from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from frontend import models
from frontend.models import contactdb, registerdb, applicationdb
from backend1.models import categorydb,companyDb
from django.contrib import messages
import random



# Create your views here.
def homepage(req):
    data=categorydb.objects.all()
    cat=registerdb.objects.filter(email=req.session['email'])
    return render(req,"index2.html",{'data':data,'cat':cat})

def aboutpage(req):
    return render(req,"about.html")

def contactpage(req):
    return render(req,"contact.html")

def findjobpage(req):
    data = categorydb.objects.all()
    return render(req,"find_jobs.html",{'data':data})

def jobdetails(request,dataid):
    data = categorydb.objects.get(id=dataid)
    cat=registerdb.objects.filter(email=request.session['email'])
    return render(request,"job_details.html",{'data':data,'cat':cat})


def save_contact(request):
    if request.method == "POST":
        msg = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        obj = contactdb(message=msg,name=name,email=email,subject=sub)
        obj.save()
        return redirect(contactpage)


def otp_verification(request):
    return render(request,"otp_verification.html")

def loginpage(req):
    return render(req,"login_page.html")

def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp(user_email, otp):
    try:
        user = registerdb.objects.get(email=user_email)
        to = str(user.email)
        subject = 'OTP - JobFinder'
        message = f'Dear {user.name},\n\nYour OTP for login is: {otp}'
        from_email = 'your_email@example.com'

        send_mail(subject, message, from_email, [to], fail_silently=False)
    except registerdb.DoesNotExist:
        print(f"User with email {user_email} not found.")

def login_user(req):
    if req.method == "POST":
        em = req.POST.get('email')
        pwd = req.POST.get('password')
        messages.success(req, "Login succesfully...!!")
        if registerdb.objects.filter(email=em,password=pwd).exists():

            otp = generate_otp()
            try:
                send_otp(em,otp)
                req.session['password'] = pwd
                req.session['email'] = em
                req.session['otp'] = otp
                return redirect(otp_verification)
            except Exception as e:
                messages.error(req,f"Error Sending OTP:{e}")
                return redirect(loginpage)
        else:
            return redirect(loginpage)
    else:
        return redirect(loginpage)


def otps_verification(request):
    if request.method == "POST":
        user_entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')

        if stored_otp and user_entered_otp == stored_otp:
            # OTP is correct, redirect to the homepage
            return redirect('homepage')
        else:
            # Incorrect OTP, display an alert in the template
            incorrect_otp_alert = True
            return render(request, "otp_verification.html", {'incorrect_otp_alert': incorrect_otp_alert})
    else:
        # Generate and store a new OTP in the session
        generated_otp =send_otp()  # Make sure you have this function defined
        request.session['otp'] = generated_otp

        # Render the template for entering OTP
        return render(request, "otp_verification.html")

def signuppage(req):
    return render(req,"signup.html")

def save_register(request):
    if request.method=="POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        m = request.POST.get('mobile')
        p = request.POST.get('password')
        r = request.FILES['resume']
        pro = request.FILES['profile']
    obj = registerdb(name=n,email=e,password=p,mobile=m,resume=r,profile=pro)
    obj.save()
    messages.success(request, "signup succesfully...!!")
    return redirect(loginpage)


def userlogout(request):
    del request.session['email']
    del request.session['password']
    return redirect(login_user)

def filtered_jobpage(req,dataid):
    data = categorydb.objects.filter(id=dataid)
    return render(req,"filtered_job.html",{'data':data})

def apply_successpage(req):
    return render(req,"apply_successpage.html")



def job_search(request):
    query = request.GET.get('q')

    if query:
        jobs = categorydb.objects.filter(models.Q(title__icontains=query) | models.Q(description__icontains=query))
    else:
        jobs = categorydb.objects.all()

    return render(request, 'job_search.html', {'jobs': jobs, 'query': query})

def searchpage(req):
    return render(req,"search_page.html")


def searching(request):
    if request.method=="POST":
        query=request.POST.get('selectcategory')
        if query:
            results=categorydb.objects.filter(jobname__contains=query)
        else:
            results=[]
    return render(request,"search_page.html",{'results':results})

def profileuser(request):
    data=registerdb.objects.filter(email=request.session['email'])
    return render(request,"profilepage.html",{'data':data})


def edituser(request,dataid):
    user=registerdb.objects.get(id=dataid)
    return render(request,"editpage.html",{'user':user})

def updateprofile(request, dataid):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        sex = request.POST.get('sex')
        address = request.POST.get('address')
        try:
            img = request.FILES['profile']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = registerdb.objects.get(id=dataid).profile
        registerdb.objects.filter(id=dataid).update(name=name, age=age, dob=dob, profile=file,sex=sex,address=address)
        return redirect(profileuser)

def editresume(request,dataid):
    data=registerdb.objects.get(id=dataid)
    return render(request,"editresume.html",{'data':data})

def resumesave(request,dataid):
    if request.method == "POST":
        try:
            img = request.FILES['resume']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = registerdb.objects.get(id=dataid).resume
        registerdb.objects.filter(id=dataid).update(resume=file)
        return redirect(profileuser)


def changepassword(request):
    data=applicationdb.objects.all()
    return render(request,"changepassword.html",{'data':data})

def updatepassword(request):
    if request.method=="POST":
        o=request.POST.get('old')
        n=request.POST.get('new')
        user = registerdb.objects.filter(email=request.session['email'], password=o).first()
        if user:
            user.password=n
            user.save()

            request.session['password'] = n
            messages.success(request, 'Password successfully changed!')
            return redirect(profileuser)
        else:
            error_message=True
            return render(request, 'changepassword.html', {'error_message':error_message})
    return render(request, 'changepassword.html')


def applicationsave(request):
    if request.method=="POST":
        job=request.POST.get('job')
        company=request.POST.get('company')
        location=request.POST.get('location')
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        resume=request.POST.get('resume')
        obj=applicationdb(job=job,company=company,location=location,name=name,email=email,mobile=mobile,address=address,resume=resume)
        obj.save()

        subject = f'{name} Your Application was sent  '
        message = f'Dear {name} , \n Your application was sent for {job} position. '
        from_email = 'your_email@example.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return redirect(homepage)


def companiesbased(request,company):
    data=categorydb.objects.filter(comapnyname=company)
    return render(request,"companiesbased.html",{'data':data})
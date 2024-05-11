from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from backend1.models import categorydb, companyDb
from frontend.models import contactdb, applicationdb
from django.contrib import messages
def index(request):
    data=companyDb.objects.filter(email=request.session['email'])
    return render(request,"index.html",{'data':data})

def addjob(request):
    data=companyDb.objects.filter(email=request.session['email'])
    return render(request,"addjob.html",{'data':data})

def displayjob(request):
    data=categorydb.objects.filter(company_id=request.session['email'])
    return render(request,"displayjob.html",{'data':data})

def companysignup(request):
    return render(request,"companysignup.html")

def companysave(request):
    if request.method=="POST":
        email=request.POST.get('email')
        companyname=request.POST.get('company')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        loaction=request.POST.get('location')
        state=request.POST.get('state')
        description=request.POST.get('description')
        profile=request.FILES['profile']
        obj=companyDb(companyname=companyname,email=email,password=password,mobile=mobile,location=loaction,state=state,description=description,profile=profile)
        obj.save()
    return redirect(companylogin)

def companylogin(request):
    return render(request,"companylogin.html")


def companysignin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_exists = companyDb.objects.filter(email=email, password=password).exists()

        if user_exists:
            request.session['email'] = email
            request.session['password'] = password
            return redirect(index)
        else:
            incorrectpass=True
            return render(request,'companylogin.html',{'incorrectpass':incorrectpass})

    return render(request, 'companylogin.html')


def companylogout(request):
    del request.session['email']
    del request.session['password']
    return redirect(companysignup)


def jobsave(request):
    if request.method=="POST":
        comapny_id=request.POST.get('id')
        comapny_name=request.POST.get('comapnyname')
        job_name=request.POST.get('name')
        job_type=request.POST.get('type')
        job_exp=request.POST.get('experience')
        job_loc=request.POST.get('location')
        job_des=request.POST.get('description')
        job_skill=request.POST.get('skill')
        job_qual=request.POST.get('qualification')
        lpa=request.POST.get('lpa')
        profile=request.POST.get('profile')
        obj=categorydb(company_id=comapny_id,comapnyname=comapny_name,jobname=job_name,jobexperience=job_exp,jobtype=job_type,joblocation=job_loc,jobdes=job_des,skills=job_skill,qualification=job_qual,lpa=lpa,profile=profile)
        obj.save()
        return redirect(addjob)


def displaycontact(request):
    return render(request,"display_contact.html")


def deletejob(request,dataid):
    obj=categorydb.objects.get(id=dataid)
    obj.delete()
    return redirect(displayjob)

def editjob(request,dataid):
    cat=categorydb.objects.get(id=dataid)
    return render(request,"editjob.html",{'cat':cat})


def jobedit(request,dataid):
    if request.method == "POST":
        job_name = request.POST.get('name')
        job_type = request.POST.get('type')
        job_exp = request.POST.get('experience')
        job_loc = request.POST.get('location')
        job_des = request.POST.get('description')
        job_skill = request.POST.get('skill')
        job_qual = request.POST.get('qualification')
        lpa = request.POST.get('lpa')
        categorydb.objects.filter(id=dataid).update(jobname=job_name,jobexperience=job_exp,jobtype=job_type,joblocation=job_loc,jobdes=job_des,skills=job_skill,qualification=job_qual,lpa=lpa)
        return redirect(displayjob)




def displayapplications(request):
    data=applicationdb.objects.filter(company=request.session['email'],reply="No Reply")
    cat = applicationdb.objects.filter(company=request.session['email'], reply__isnull=False).exclude(reply="No Reply")


    return render(request,"displayapplications.html",{'data':data,'cat':cat})


def companyprofile(request):
    data=companyDb.objects.filter(email=request.session['email'])
    return render(request,"companyprofile.html",{'data':data})




def sendreply(request,dataid):
    data=applicationdb.objects.get(id=dataid)
    return render(request,"sendreply.html",{'data':data})


def applicantreply(request,dataid):
    if request.method=="POST":
        em=request.POST.get('email')
        me=request.POST.get('rmes')
        applicationdb.objects.filter(id=dataid).update(reply=me)

        job=applicationdb.job
        subject = f'Your Application for {job} is {me}'
        message = f'{me}'
        from_email = 'your_email@example.com'  # Replace with your email address
        recipient_list = [em]  # Use the entered email address as the recipient

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return redirect(displayapplications)

    return render(request, 'error_page.html',{'message_sent': False})

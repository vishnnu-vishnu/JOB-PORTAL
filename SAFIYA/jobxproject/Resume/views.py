from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from reportlab.pdfgen import canvas


from Resume.models import clientDb


# Create your views here.
def clientdetails(request):
    return render(request,"add_clientdetails.html")



def client_save(req):
    if req.method == "POST":
        cn = req.POST.get('name')
        ce = req.POST.get('email')
        cp = req.POST.get('phone')
        ca = req.POST.get('address')
        cv = req.FILES['resume']
        obj = clientDb(name=cn, email=ce, phone=cp, addrs=ca, resume=cv)
        obj.save()
        subject = "Job finder"
        messages = "your application submitted successfully "
        from_email = 'aswing9002@gmail.com'
        recipient_list = [ce]
        send_mail(subject, messages, from_email, recipient_list, fail_silently=False)
    return redirect(resumesucess)

def viewpdf(request):
    pdf_file=clientDb.objects.last()
    return render(request,'view_pdf.html',{'pdf_file':pdf_file})

def disp_clientdetais(req):
    data = clientDb.objects.all()
    return render(req,"display_details.html",{'data':data})

def resumesucess(request):
    return render(request,"application_sucess.html")


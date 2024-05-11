from django.contrib import admin
from django.urls import path
from backend1 import views


urlpatterns = [
    path("index/",views.index,name="index"),
    path('addjob/', views.addjob, name="addjob"),
    path('displayjob/', views.displayjob, name="displayjob"),
    path('companysignup/',views.companysignup,name="companysignup"),
    path('companysave/',views.companysave,name="companysave"),
    path('',views.companylogin,name="companylogin"),
    path('companysignin/',views.companysignin,name="companysignin"),
    path('jobsave/',views.jobsave,name="jobsave"),
    path('displayapplications/',views.displayapplications,name="displayapplications"),
    path('companyprofile/',views.companyprofile,name="companyprofile"),
    path('sendreply/<int:dataid>/',views.sendreply,name="sendreply"),
    path('applicantreply/<int:dataid>/',views.applicantreply,name="applicantreply"),
    path('acompanylogout/',views.companylogout,name="companylogout"),
    path('editjob/<int:dataid>/',views.editjob,name="editjob"),
    path('deletejob/<int:dataid>/',views.deletejob,name="deletejob"),
    path('jobedit/<int:dataid>/',views.jobedit,name="jobedit"),
    path('displaycontact/',views.displaycontact,name="displaycontact"),

]
from django.contrib import admin
from django.urls import path

from frontend import views

urlpatterns= [
    path('homepage/',views.homepage,name="homepage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('findjobpage/',views.findjobpage,name="findjobpage"),
    path('jobdetails/<int:dataid>/',views.jobdetails,name="jobdetails"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('',views.loginpage,name="loginpage"),
    path('signuppage/',views.signuppage,name="signuppage"),
    path('save_register/',views.save_register,name="save_register"),
    path('login_user/',views.login_user,name="login_user"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('filtered_jobpage/<int:dataid>/',views.filtered_jobpage,name="filtered_jobpage"),
    path('apply_successpage/',views.apply_successpage,name="apply_successpage"),
    path('job_search/',views.job_search,name="job_search"),
    path('searchpage/',views.searchpage,name="searchpage"),
    path('searching/',views.searching,name="searching"),
    path('profileuser/',views.profileuser,name="profileuser"),
    path('edituser/<int:dataid>/',views.edituser,name="edituser"),
    path('updateprofile/<int:dataid>/',views.updateprofile,name="updateprofile"),
    path('resumesave/<int:dataid>/',views.resumesave,name="resumesave"),
    path('editresume/<int:dataid>/',views.editresume,name="editresume"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('updatepassword/',views.updatepassword,name="updatepassword"),
    path('applicationsave/',views.applicationsave,name="applicationsave"),
    path('otp_verification/',views.otp_verification,name="otp_verification"),
    path('otps_verification/',views.otps_verification,name="otps_verification"),
    path('companiesbased/<company>/',views.companiesbased,name="companiesbased"),

]
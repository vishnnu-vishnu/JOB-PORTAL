from Resume import views
from django.urls import path



urlpatterns= [
    path('clientdetails/',views.clientdetails,name="clientdetails"),
    path('client_save/',views.client_save,name="client_save"),
    path('disp_clientdetais/',views.disp_clientdetais,name="disp_clientdetais"),
    path('resumesucess/',views.resumesucess,name="resumesucess",),
    path('viewpdf/',views.viewpdf,name="viewpdf"),


]
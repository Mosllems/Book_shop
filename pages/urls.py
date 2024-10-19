from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path("contactus/", views.ContactUsview.as_view(), name="contactus"),
    path("aboutus/", views.AboutUsView.as_view(), name="aboutus"),

    ]

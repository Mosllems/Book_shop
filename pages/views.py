from django.shortcuts import render
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = "home.html"


class ContactUsview(generic.TemplateView):
    template_name = "pages/contactus.html"


class AboutUsView(generic.TemplateView):
    template_name = "pages/aboutus.html"


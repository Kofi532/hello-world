from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render




class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):  # new
    template_name = "about.html"

class ServicePageView(TemplateView):
    template_name = "service.html"








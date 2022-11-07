from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
import os
from pathlib import Path
import ctypes  # An included library with Python install.



class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):  # new
    template_name = "about.html"

class ServicePageView(TemplateView):
    template_name = "service.html"


class HoPageView(TemplateView):
    template_name = "your-name.html"

def uploadImg(request):
    
    image_list=[]

    for root, dirs, files in os.walk(settings.MEDIA_ROOT):
        for file in files:
            image_list.append(file)
    return render(request, 'your-name.html',{'brands': image_list})






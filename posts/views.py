from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post, Experience
from django.urls import reverse_lazy  # new

from django.views import generic
from .forms import PostForm

class HomePageView(ListView):
    model = Post
    template_name = "posthome.html"
    success_url = reverse_lazy("/")

class CreatePostView(CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = "post.html"
    success_url = reverse_lazy("post.html")

class ExperienceList(generic.ListView):
    model = Experience
    template_name = 'posthome.html'
    queryset = Experience.objects.all()
# Create your views here.

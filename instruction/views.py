from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import *


class HomeView(ListView):
    template_name = 'instruction/index.html'
    model = Post
    context_object_name = 'post'

class PostView(DetailView):
    template_name = 'instruction/post_detail.html'
    model = Post
    slug_url_kwarg = 'instr'
    context_object_name = 'post'



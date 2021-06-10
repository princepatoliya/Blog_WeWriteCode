from django.shortcuts import render
from django.http import HttpResponse

from .form import (
    BlogForm
    )
# Create your views here.

def home_screen_view(request):
    return render(request, 'home/home.html')


def add_blog(request):
    data = {
    'form' : BlogForm
    }
    return render(request, 'home/add_blog.html', data)




    
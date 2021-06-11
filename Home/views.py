from django.shortcuts import render
from django.http import HttpResponse

from .models import (
    BlogModel
    )

from .form import (
    BlogForm
    )
# Create your views here.

def home_screen_view(request):
    data = {
    'blogs' : BlogModel.objects.all(),
    }
    return render(request, 'home/home.html', data)


def add_blog(request):
    try:
        if request.method == "POST":
            print("-------------------------i'm working------------------------------")
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['uploadedimage']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']


            blog_obj = BlogModel.objects.create(user=user, title=title, content=content, image=image)

    except Exception as e:
        print(e) 


    data = {
    'form' : BlogForm
    }

    return render(request, 'home/add_blog.html', data)




    
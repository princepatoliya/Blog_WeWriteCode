from django.shortcuts import render
from django.http import HttpResponse

from django.contrib import messages

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
            # print("-------------------------i'm working------------------------------")
            form = BlogForm(request.POST)
            # print(request.FILES)
            image = request.FILES['uploadedimage']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']


            blog_obj = BlogModel.objects.create(user=user, title=title, content=content, image=image)
            messages.info(request, f"{title} - Blog published successfully")
            return render(request, 'home/home.html')

    except Exception as e:
        print(e) 


    data = {
    'form' : BlogForm
    }

    return render(request, 'home/add_blog.html', data)


def blog_detail(request, slug):
    print("slug:", slug)
    try:
        data = {'blog_detail': BlogModel.objects.filter(slug = slug).first()}
        print("data: ", data)

    except Exception as e:
        print(e)

    
    return render(request, "home/blog_detail.html", data)



def your_all_blogs(request):
    data = {}
    try: 
        blogs = BlogModel.objects.filter(user = request.user)
        data = {'all_blogs' : blogs}
    
    except Exception as e:
        print(e)

    return render(request, "home/your_all_blogs.html", data)
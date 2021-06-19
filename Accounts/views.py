from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Profile
from Home.models import BlogModel

# Create your views here.

def register_view(request):
    if request.user.is_authenticated:
        messages.info(request, f"Dear {request.user} you are already registered and logged in")
        return redirect('home')
    else:
        return render(request, 'accounts/register.html')

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, f"Dear {request.user} you are already logged in")
        return redirect('home')
    else:
        return render(request, 'accounts/login.html')

@login_required(login_url='login_view')
def profile_view(request):
    data = {}
    try: 
        blogs = BlogModel.objects.filter(user = request.user)
        data = {'all_blogs' : blogs}
    
    except Exception as e:
        print(e)
    return render(request, "accounts/profile.html",data)



def verify_view(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(token = auth_token).first()

        if profile_obj:
            if profile_obj.is_verified:
                messages.info(request, "Your account is already verified.")
                return redirect('login_view')
            
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, "Your Account has been verified.")
            return redirect('login_view')
        else:
            messages.warning(request, "Invalid token detected.")
            return redirect('login_view')
            

    except Exception as e:
        print(e)
        return redirect('login_view')
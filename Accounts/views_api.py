from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import Profile

from Home.helper import generate_random_string, send_email_after_register

import uuid

from django.contrib.auth import authenticate, login

from django.contrib import messages

class LoginView(APIView):
    

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something Went Wrong'

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'Key username not found' 
                raise Exception("Key username not found ")
            
            if data.get('password') is None:
                response['message'] = 'Key password not found'
                raise Exception("Key password not found")
                

            check_user = User.objects.filter(username = data.get('username')).first()
            
            if check_user is None:
                response['message'] = 'Invalid credentials'
                raise Exception('User not found')

            if not Profile.objects.filter(user = check_user).first().is_verified:
                response['message'] = 'Account is not verify. check your mail'
                raise Exception("Account is not verify. check your mail")
            

            user_obj = authenticate(username = data.get('username'), password = data.get('password'))
            
            if user_obj:
                login(request, user_obj)
                response['message'] = 'Welcome'
                response['status'] = 200
                messages.success(request, f"{data.get('username')} - Welcome ")
            else:
                response['message'] = 'Invalid credentials'
                raise Exception('Invalid password')

        except Exception as e:
            print(e)
        
        return Response(response)

LoginView = LoginView.as_view() 

class RegisterView(APIView):
    
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = "Something went wrong"    

        try: 
            data = request.data

            if data.get('username') is None:
                response['message'] = "Key username is not found"
                raise Exception("Key username is not found")
            
            if data.get('password') is None:
                response['message'] = "Key password is not found"
                raise Exception("Key password is not found")

            if data.get('confirmpassword') is None:
                response['message'] = "Key confirmpassword is not found"
                raise Exception("Key confirmpassword is not found")
            
            if data.get('email') is None:
                response['message'] = "Key email is not found"
                raise Exception("Key email is not found")
            
            if data.get('password') != data.get('confirmpassword'):
                response['message'] = "Password and confirm-password must match"
                raise Exception("Password and confirm-password must match")

            user_check = User.objects.filter(username = data.get('username')).first()

            if user_check:
                response['message'] = "Username is already exists"
                raise Exception('Username is alredy exists')
            
            user_check = User.objects.filter(email = data.get('email')).first()

            if user_check:
                response['message'] = "Email-id is already registered."
                raise Exception('Email-id is already registered.')
            
            user_obj = User.objects.create(username=data.get('username'), email=data.get('email'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            
            verify_token = str(uuid.uuid4())

            profile_obj = Profile.objects.create(user = user_obj, token = verify_token)
            profile_obj.save()
            send_email_after_register(data.get('email'), verify_token)


            user_obj.save()

            response['message'] = "User created"
            response['status'] = 200
            
        except Exception as e:
            print(e)
        
        return Response(response)


RegisterView = RegisterView.as_view()

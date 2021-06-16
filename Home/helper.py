from django.utils.text import slugify

from django.conf import settings

from django.core.mail import EmailMessage

#generate random string
import random
import string
def generate_random_string(n):
    return ' ' + ''.join(random.choices(string.ascii_uppercase + string.ascii_letters, k=n))


#Generate new slug if exicts then call same function and add random string with text
def generate_slug(text):
    new_slug = slugify(text)
    
    #import here because circular import issue
    from .models import BlogModel
    if BlogModel.objects.filter(slug = new_slug).first():
        return generate_slug(text + generate_random_string(random.randint(1,9)) )
    
    # print("finally:-  ", new_slug)
    return new_slug


def send_email_after_register(user_email, verify_token):
    try:
        email = EmailMessage(
            "WE WRITE CODE : Account verification",
            f"Thank you for registering with us. You are now part of a great community. Please click on this link to verify your account http://127.0.0.1:8000/accounts/verify/{verify_token}",
            settings.EMAIL_HOST_USER,
            [user_email],
        )
        email.fail_silently = False
        email.send()
        return True


    except Exception as e:
        print("While sending email this error accours: ", e)
        return False
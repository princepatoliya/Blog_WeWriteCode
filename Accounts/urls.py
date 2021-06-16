from django.urls import path
from .views import (
    login_view,
    register_view,
    verify_view,
)

urlpatterns = [
    path('login/', login_view, name="login_view"),
    path('register/', register_view, name="register_view"),
    path('verify/<auth_token>', verify_view, name="verify_view")
]
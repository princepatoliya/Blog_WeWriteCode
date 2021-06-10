
from django.urls import path, include
from .views import (
    add_blog,
    home_screen_view,
)

urlpatterns = [
    path('', home_screen_view, name="home"),
    path('add_blog/', add_blog, name="add_blog")
]
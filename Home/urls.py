
from django.urls import path
from .views import (
    logout_view,
    add_blog,
    delete_blog,
    update_blog,
    home_screen_view,
    blog_detail,
)

urlpatterns = [
    path('', home_screen_view, name="home"),
    path('logout_view/', logout_view, name="logout_view"),
    path('add_blog/', add_blog, name="add_blog"),
    path('delete_blog/<int:id>/', delete_blog, name="delete_blog"),
    path('update_blog/<slug>', update_blog, name="update_blog"),
    path('blog_detail/<slug>/', blog_detail, name="blog_detail"),
]
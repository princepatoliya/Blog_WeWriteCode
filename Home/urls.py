
from django.urls import path, include
from .views import (
    add_blog,
    delete_blog,
    update_blog,
    home_screen_view,
    blog_detail,
    your_all_blogs,
)

urlpatterns = [
    path('', home_screen_view, name="home"),
    path('add_blog/', add_blog, name="add_blog"),
    path('delete_blog/<int:id>/', delete_blog, name="delete_blog"),
    path('update_blog/<slug>', update_blog, name="update_blog"),
    path('blog_detail/<slug>/', blog_detail, name="blog_detail"),
    path('your_all_blogs/', your_all_blogs, name="your_all_blogs")
]
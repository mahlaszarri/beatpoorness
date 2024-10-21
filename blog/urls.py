from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("blogs/<slug:slug>", views.blog_detail, name="blog_detail"),
    path("search_blog/",views.search_blog, name="search_blog"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]

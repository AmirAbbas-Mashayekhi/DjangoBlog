from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:blog_id>', views.blog_info, name='blog_info'),
]
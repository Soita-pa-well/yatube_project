from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='post_index'),
    path('group/<slug:slug>/', views.group_posts, name='post_group_posts'),
    path('group_list/', views.group_list, name='post_group_list')
]

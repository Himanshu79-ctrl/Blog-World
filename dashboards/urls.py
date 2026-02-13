from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    #category crud urls
    path('categories/', views.categories, name='categories'),
    path('category/add/', views.add_category, name='add_category'),  
    path('category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('category/delete/<int:pk>/', views.delete_category, name='delete_category'),    

    #blog crud urls
    path('posts/', views.posts, name='posts'), 
    path('post/add/', views.add_post, name='add_post'),  
    path('post/edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('post/delete/<int:pk>/', views.delete_post, name='delete_post'),

    #user management urls
    path('users/', views.users, name='users'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/edit/<int:pk>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:pk>/', views.delete_user, name='delete_user'),
]
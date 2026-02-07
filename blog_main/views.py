from django.shortcuts import render
from about_us.models import About
from blogs.models import Blog, Category

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    
    #fetch the about us content
    try:
        about_us = About.objects.get()
    except About.DoesNotExist:
        about_us = None


    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about_us': about_us,
    }
    return render(request, 'home.html', context)
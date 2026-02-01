from django.shortcuts import render
from blogs.models import Blog, Category

def home(request):
    catagories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    print(posts)
    context = {
        'catagories': catagories,
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html', context)
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category
# Create your views here.

def posts_by_category(request, category_id):
    #fetch the post that belongs to the category witt the id category_id
    post = Blog.objects.filter(category__id=category_id, status='Published')
    try:
        category = Category.objects.get(id=category_id)
    except:
        #if the category does not exist, return to the home page
        return redirect('home')
    #category = get_object_or_404(Category, id=category_id)
    context={
        'post': post,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)
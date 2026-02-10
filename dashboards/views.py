from django.shortcuts import render, redirect
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm  


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'dashboard/categories.html', context)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    forms = CategoryForm()
    context = {
        'forms': forms,
    }
    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category) #request.data = new values, instance = old values
        if form.is_valid():
            form.save()
            return redirect('categories')
    forms = CategoryForm(instance=category)
    context = {
        'forms': forms,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)

def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('categories')
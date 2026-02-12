from django.shortcuts import render, redirect
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from .forms import BlogPostForm, CategoryForm  
from django.template.defaultfilters import slugify


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



def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Create a Blog instance but don't save to the database yet
            post.author = request.user  # Set the author to the currently logged-in user
            post.save()  # Save the Blog instance to the database to generate an ID that id is used to generate unique slug
            title = form.cleaned_data['title']  # Get the title from the form data
            post.slug = slugify(title) + '-' + str(post.id)  # Generate a slug from the title and append post ID to ensure uniqueness   
            post.save() 
            return redirect('posts')
        else:
            print(form.errors)

    forms = BlogPostForm()
    context = {
        'forms': forms,
    }
    return render(request, 'dashboard/add_post.html', context)


def edit_post(request, pk):
    post = Blog.objects.get(id=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post) #request.data = new values, instance = old values
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']  # Get the title from the form data
            post.slug = slugify(title) + '-' + str(post.id)  # Generate a slug from the title and append post ID to ensure uniqueness   
            post.save()      
            return redirect('posts')
    forms = BlogPostForm(instance=post)
    context = {
        'forms': forms,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html', context)


def delete_post(request, pk):
    post = Blog.objects.get(id=pk)
    post.delete()
    return redirect('posts')
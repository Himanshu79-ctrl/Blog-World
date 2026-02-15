from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category, Comment
from django.db.models import Q  #for search functionality, jaise ',' and ke jaise behave karta hai , isliye ham 'or' functionality ke liye Q ka use karte hain



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

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST.get('comment')
        comment.save()
        return redirect('blogs', slug=slug)
    #comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published') #yaha par ',' and ke jaise behave karega, isliye ham 'or' functionality ke liye Q ka use karte hain, jisse ham title me keyword ke alawa content me bhi keyword search kar sakte hain
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)



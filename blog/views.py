from django.shortcuts import render
from .decorators import get_blog2
from .models import Eblog, Category, Post
# Create your views here.
@get_blog2
def home(request, blog, theme):
    posts = Post.objects.filter(blog=blog).order_by('-id')
    category = Category.objects.filter(blog=blog)

    context = {
        'category': category,
        'latest': posts[:12],
        'trending': posts.filter(trending=True)[:5],
        'featured': []
    }
    featured = Category.objects.filter(blog=blog, featured=True)
    print(featured, 77)
    for cat in featured:
        postList = Post.objects.filter(blog=blog, category=cat).order_by('-id')
        if not postList:
            continue
        obj = {
            'name': cat.name,
            'posts': postList
        }
        context['featured'].append(obj)

    return render(request, theme.path + '/home.html', context)

@get_blog2
def blog_details(request, blog, theme):
    id = request.GET.get('id', None)
    post = Post.objects.get(id=id)
    context = {
        'post': post,
        'related': Post.objects.filter(category=post.category)[:10],
        'category': Category.objects.filter(blog=blog),
    }
    return render(request, theme.path + '/blog_details.html', context)

@get_blog2
def categories(request, blog, theme,  category_id):
    category = Category.objects.filter(blog=blog)

    context = {
        'featured': [],
        'category': category
    }
    featured = Category.objects.filter(blog=blog, featured=True, id=category_id)
    for cat in featured:
        postList = Post.objects.filter(blog=blog, category=cat).order_by('-id')
        postsnum = postList.count()
        print(postsnum)
        if not postList:
            continue
        obj = {
            'name': cat.name,
            'posts': postList,
            'postsnum': postsnum,
        }
        context['featured'].append(obj)
        
    return render(request, theme.path + '/categories.html', context)

@get_blog2
def pages(request, blog, theme):
    return render(request, theme.path + '/pages.html')

@get_blog2
def search(request, blog, theme):
    return render(request, theme.path + '/search.html')

@get_blog2
def about(request, blog, theme):
    return render(request, theme.path + '/about.html')

@get_blog2
def account(request, blog, theme):
    return render(request, theme.path + '/account.html')

@get_blog2
def contact(request, blog, theme):
    return render(request, theme.path + '/contact.html')
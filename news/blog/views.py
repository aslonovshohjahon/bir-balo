from django.shortcuts import *
from .models import *
from .forms import *
from django.db.models import Q 
from django.urls import reverse

def search(request):
    query = request.GET.get('search')
    search_obj = Post.objects.filter(
        Q(title__icontains=query)
    )
    return render(request, 'blog/search.html', {'search_obj':search_obj})


def index(request):
    posts = Post.objects.order_by('-date')[:3]
    return render(request, 'blog/index.html', {'posts':posts})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts':posts})

def post(request, id):
    post = Post.objects.get(id=id)
    post.pro += 1
    post.save()
    return render(request, 'blog/post.html', {'post':post})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories':categories})


def category(request, id):
    category = Category.objects.get(id=id)
    post = Post.objects.filter(category=category).order_by("-date")
    return render(request, 'blog/category.html', {'category':category, 'post':posts})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/index.html')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form':form})



def comment(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.comment_set.create(
            user = request.user,
            text = request.POST.get('text')
        )
        return redirect(reverse ('post', kwargs = {'id':post.id})) 
    return redirect(reverse ('post', kwargs = {'id':post.id}))  
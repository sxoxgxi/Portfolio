from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import redirect
# from django.http import HttpResponse
from .models import User, Post, Comment


def index(request):
    return render(request, 'base/home.html')


def blog(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'base/blog.html', context)


def blog_detail(request, id):
    post = Post.objects.get(id=id)
    comments = post.comment_set.all()
    context = {'post': post, 'comments': comments}
    return render(request, 'base/blog_detail.html', context)


def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
        except Exception as e:
            context = {'error': e}
            return render(request, 'base/error.html', context, status=401)
        if user is not None:
            login(request, user)
            return redirect('home')

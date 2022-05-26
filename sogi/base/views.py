from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
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


def login(request):
    return HttpResponse("<center><p>404 Not Found</p> Try again later <p> <img src='https://media1.tenor.com/images/bd900a9a994238168c8e843cc3a575a6/tenor.gif' alt='Not found'></p></center>", status=404)

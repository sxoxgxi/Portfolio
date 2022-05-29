from django.contrib.auth import authenticate, login, logout
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
    page = "login"
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        try:
            user = User.objects.get(username=username)
        except:
            context = {
                'error': 'Please enter the correct username and password. Note that both fields may be case-sensitive.',
                'status': '401 - Unauthenticated'
                }
            return render(request, 'base/error.html', context, status=401)
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {
                'error': 'Please enter the correct username and password. Note that both fields may be case-sensitive.',
                'status': '401 - Unauthenticated'
                }
            return render(request, 'base/error.html', context, status=401)
    
    return render(request, 'base/login.html', {'page': page})

def logoutView(request):
    logout(request)
    return redirect('home')


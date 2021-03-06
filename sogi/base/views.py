from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from .models import User, Post, Comment
from .forms import MyUser, Blog
from .faxs import get_quote


def index(request):
    return render(request, 'base/home.html')


def blog(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'base/blog.html', context)


def blog_detail(request, id):
    post = Post.objects.get(id=id)
    comments = post.comment_set.all()
    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            post=post,
            body=request.POST.get('comment')
        )
        # return redirect('blog_detail', post.id)
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


@csrf_protect
def registerView(request):
    form = MyUser()
    context = {'form': form,
               "error": "The server is unavailable to handle this request right now. Something went wrong while processing the request. Try again later.",
               'status': '503 - Service Unavailable'}
    if request.method == 'POST':
        form = MyUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, "base/error.html", context, status=503)
    return render(request, "base/login.html", context)


def logoutView(request):
    logout(request)
    return redirect('home')


def profileView(request, id):
    user = User.objects.get(id=id)
    quote = get_quote()[0]
    author = get_quote()[1]
    context = {'user': user, 'quote': quote, 'author': author}
    return render(request, "base/profile.html", context)


def createView(request):
    form = Blog()
    if request.method == 'POST':
        post = Post.objects.create(
            author=request.user,
            title=request.POST.get('title'),
            content=request.POST.get('content'),
        )
    context = {'form': form}
    return render(request, "base/create.html", context)

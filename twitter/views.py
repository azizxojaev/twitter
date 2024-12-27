from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'page': 'home'
    }
    return render(request, 'home.html', context=context)

def create_post_page(request):
    if request.user.is_authenticated:
        context = {
            'page': 'create'
        }

        return render(request, 'create.html', context=context)
    else:
        return redirect('register')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context = {
            'page': 'login'
        }
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('home')
            else:
                context['error'] = 'Username already taken!'

        return render(request, 'register.html', context=context)
    

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context = {
            'page': 'login'
        }
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                context['error'] = "Incorrect username or password"
    
    return render(request, 'login.html', context=context)


def logout_page(request):
    logout(request)
    return redirect('register')
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'page': 'home'
    }
    return render(request, 'home.html', context=context)

def create_post_page(request):
    print(request.user.is_authenticated)
    context = {
        'page': 'create'
    }
    return render(request, 'create.html', context=context)
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'url': 'home'
    }
    return render(request, 'home.html', context=context)
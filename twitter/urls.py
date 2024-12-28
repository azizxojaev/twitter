from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('create/', create_post_page, name='create'),
    path('register/', register_page, name='register'),
    path('my-posts/', my_post_page, name='my_posts'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]
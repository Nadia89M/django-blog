from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'title' : 'Blog Posts',
        'posts' : posts
    }
    return render(request, 'posts/index.html', context)

def post(request, post_id):
    # post = Posts.objects.get(id=id)
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post' : post
    }
    return render(request, 'posts/post.html', context)

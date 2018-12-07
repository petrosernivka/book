from django.shortcuts import render
from post.models import Post, Comments

# Create your views here.

def posts(request):
    return render(request, 'posts/posts.html', context={'posts': Post.objects.all()})

def post(request, post_id=1):
    return rendere(request, 'posts/post.html', context={'post': Post.objects.get(id=post_id), 'comments': Comments.objects.filter(comments_posts_id=post_id)})

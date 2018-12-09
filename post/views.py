# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from datetime import datetime
from post.models import Post, Comments
from post.forms import CommentForm

# Create your views here.

def posts(request):
    return render(request, 'posts/posts.html', context={'posts': Post.objects.all(), 'username': auth.get_user(request).username})


def post(request, post_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['post'] = Post.objects.get(id=post_id)
    args['comments'] = Comments.objects.filter(comments_post_id=post_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render(request, 'posts/post.html', context=args)


def addlike(request, post_id):
    try:
        if post_id + "l" not in request.COOKIES:
            post = Post.objects.get(id=post_id)
            post.post_likes += 1
            post.save()
            response = redirect('/')
            response.set_cookie(post_id + "l", "cookie_like")
            return response
        else:
            redirect('/')
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def addunlike(request, post_id):
    try:
        if post_id + "u" not in request.COOKIES:
            post = Post.objects.get(id=post_id)
            post.post_unlikes += 1
            post.save()
            response = redirect('/')
            response.set_cookie(post_id + "u", "cookie_unlike")
            return response
        else:
            redirect('/')
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def addcomment(request, post_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_post = Post.objects.get(id=post_id)
            comment.comments_date = datetime.now()
            comment.comments_author = User.objects.get(id=request.user.id)
            form.save()
            request.session.set_expiry(10)
            request.session['pause'] = True
    return redirect('/posts/get/{}/'.format(post_id))

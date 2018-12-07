# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib import auth

# Create your views here.

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Користувач не знайдений"
            return render(request, 'login.html', context=args)
    else:
        return render(request, 'login.html', context=args)


def logout(request):
    auth.logout(request)
    return redirect('/')

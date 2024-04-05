from django.shortcuts import render, redirect
from .forms import SignUpForm, Loginform
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.set_password(form.cleaned_data.get('password'))
            save_form.save()
            auth.login(request, save_form)
            return JsonResponse({'status': 'success'})


def login(request):
    form = Loginform()
    if request.method == 'POST':

        form = Loginform(request, data = request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return JsonResponse({'status': 'success'})


def signout(request):
    logout(request)
    return redirect("home")


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .models import UserProfile
from .forms import RegisterUserForm, LoginUserForm


def index(request):
    if auth.get_user(request).is_authenticated:
        return redirect('home')
    return render(request, 'account/index.html')


def home(request):
    return render(request, 'account/home.html')


def profile(request, username):
    if username == request.user.username:
        user = UserProfile.objects.get(username=username)

        context = {
            'user': user
        }
        return render(request, 'account/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            user = authenticate(
                username=new_user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('home')
    else:
        form = RegisterUserForm(request.POST or None)
    return render(request, 'account/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        login_form = LoginUserForm(request, request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(
                username=username, password=password
            )
            if user:
                login(request, user)
                return redirect('home')
    else:
        login_form = LoginUserForm()
    return render(request, 'account/login.html', {'login_form': login_form})
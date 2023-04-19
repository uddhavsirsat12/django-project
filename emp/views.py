from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


from django.contrib import messages
from .forms import UserForm


@login_required(login_url='/login/')
def home(request):
    context = {}
    context['users'] = User.objects.all()
    return render(request, 'home.html', context)


def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['message'] = "logged In Successfully"
            return HttpResponseRedirect('/home', context)
        # else:
        #     context['error'] = "Invalid credentials"
        #     return render(request, 'login.html', context)
        #     messages.success(request, 'Logged in successfully')
        #     return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html')
        print(password)
    if request.method == 'GET':
        return render(request, 'login.html')


@login_required(login_url='/login/')
def sucess(request):
    context = {}
    context['user'] = request.user
    return render(request, 'sucess.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def signup(request):
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            user_form.save()
            context['message'] = "Signed In Successfully"
        #     return HttpResponseRedirect(reverse('login'))
        # else:
        #     context['error'] = "Invalid Form Info"
        #     messages.success(request, 'Signed in successfully')
        #     return HttpResponseRedirect(reverse('login'))
        else:
            messages.success(request, 'Invalid Form Info')
            return HttpResponseRedirect(reverse('signup'))
    else:
        context['user_form'] = UserForm
        return render(request, 'signup.html', context)

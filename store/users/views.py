from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

User = get_user_model()


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:index'))

    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем с успешной регистрацией!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(
            instance=request.user, data=request.POST, files=request.FILES,
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))

    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)

    context = {
        'title': 'Store - профиль',
        'form': form,
        'baskets': baskets,
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))

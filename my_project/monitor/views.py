from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from .models import Website


def home(request):
    return render(request, 'monitor/home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Парольдер сәйкес келмейді')
    return render(request, 'monitor/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Қате логин немесе пароль')
    return render(request, 'monitor/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    if request.method == 'POST' and 'add' in request.POST:
        Website.objects.create(
            user=request.user,
            name=request.POST['name'],
            url=request.POST['url']
        )
        messages.success(request, 'Сайт қосылды!')
        return redirect('dashboard')

    if request.method == 'POST' and 'check' in request.POST:
        website = Website.objects.get(id=request.POST['check'], user=request.user)
        response = requests.get(website.url, timeout=10)
        current_content = response.text[:500]

        if website.last_content and website.last_content != current_content:
            website.change_count += 1
            messages.warning(request, f'ӨЗГЕРІС АНЫҚТАЛДЫ! {website.name}')

        website.last_content = current_content
        website.save()
        messages.success(request, f'{website.name} тексерілді')
        return redirect('dashboard')

    if request.method == 'POST' and 'delete' in request.POST:
        website = Website.objects.get(id=request.POST['delete'], user=request.user)
        website.delete()
        messages.success(request, 'Сайт жойылды')
        return redirect('dashboard')

    websites = Website.objects.filter(user=request.user)
    return render(request, 'monitor/dashboard.html', {'websites': websites})
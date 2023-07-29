from django.shortcuts import render, redirect
from crud_app.form import CustomUserForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone


def index(request):
    return render(request, 'index.html')


def login_page(request):
    if request.user.is_authenticated and request.method == 'GET':
        return redirect('/')
    else:
        if request.method == 'POST':
            logging_username = request.POST.get('username')
            logging_password = request.POST.get('password')
            user = authenticate(
                request, username=logging_username, password=logging_password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('login')
        return render(request, 'login.html')


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')


def reg(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('/')
    return render(request, 'register.html', {'form': form})


def crud_page(request):
    if request.user.is_authenticated:
        data = Note.objects.filter(user=request.user)
        return render(request, 'Crud_template/crud_page.html', {'data': data})
    return redirect('/')


def crud_single(request, id):
    if request.user.is_authenticated:
        cs = Note.objects.get(id=id)
        return render(request, 'Crud_template/crud_single.html', {'cs': cs})
    return redirect('/')


def info_insert_view(request):
    if request.user.is_authenticated and request.method == 'GET':
        return render(request, 'Crud_template/crud_insert.html')
    return redirect('/')


def info_insert(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            user_id = request.user
            da = Note.objects.create(
                user=user_id, title=title, description=description)
            da.save()
            return redirect('crud')
    return redirect('/')


def info_update_view(request, id):
    if request.user.is_authenticated:
        cs = Note.objects.get(id=id)
        return render(request, 'Crud_template/crud_update.html', {'cs': cs})
    return redirect('/')


def info_update(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            info_id = request.POST.get('pid')
            title = request.POST.get('title')
            description = request.POST.get('description')
            da = Note.objects.get(id=info_id)
            if da.description == description and da.title == title:
                return redirect('crud')
            else:
                da.title = title
                da.description = description
                da.created_date = timezone.now()
                da.save()
                return redirect('crud')
    return redirect('/')


def info_delete(request, id):
    if request.user.is_authenticated:
        cs = Note.objects.get(id=id)
        cs.delete()
        return redirect('crud')
    return redirect('/')

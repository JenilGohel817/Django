from atexit import register
from distutils.log import error
from operator import ge
from tkinter import E
from tkinter.tix import STATUS
from django.shortcuts import render, redirect
from .forms import ContectForm
from .models import ContectModel
from django.contrib import messages
from django.http import JsonResponse


def index(request):
    if request.method == 'POST':
        form = ContectForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            picture = form.cleaned_data['picture']
            gender = form.cleaned_data['gender']
            user_find = ContectModel.objects.filter(name=name).exists()
            if user_find:
                print('------------------------------>, user name exists')
                return redirect('index')
            registerForm = ContectModel(
                name=name, email=email, password=password, picture=picture, gender=gender)
            registerForm.save()
            return JsonResponse({"name": name, "email": email, "password": password, "gender": gender}, STATUS=200)
            form = ContectForm()
        else:
            return JsonResponse({"error": error}, STATUS=400)
            form = ContectForm()
    else:
        form = ContectForm()
    i = ContectModel.objects.all()
    context = {'form': form, 'i': i}
    return render(request, 'index.html', context)


def update(request, id):
    if request.method == 'POST':
        fetch = ContectModel.objects.get(pk=id)
        form = ContectForm(request.POST, request.FILES, instance=fetch)
        if form.is_valid():
            form.save()
        return render(request, 'in.html')
    else:
        fetch = ContectModel.objects.get(pk=id)
    form = ContectForm(instance=fetch)
    context = {'form': form}
    return render(request, 'in.html', context)


def inX(request):
    return render(request, 'in.html')


def delete(request, id):
    if request.method == 'GET':
        fetch = ContectModel.objects.get(pk=id)
        fetch.delete()
    return render(request, 'inc.html')

from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import FunctionStd
from .models import FunctionUser
from django.contrib import messages


# Create your views here.
def f_add(request):
    if request.method == 'POST':
        fm = FunctionStd(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            stg = fm.cleaned_data['gender']
            check = FunctionUser.objects.filter(name=nm).exists()
            if check:
                messages.success(request, 'User Name already exists !')
                return redirect('f_add')
            reg = FunctionUser(name=nm, email=em, password=pw, gender=stg)
            reg.save()
            messages.success(request, 'profile added successfully.')
            fm = FunctionStd()
    else:
        fm = FunctionStd()
    stud = FunctionUser.objects.all()
    return render(request, 'f_add.html', {'form': fm, 'stu': stud})


def f_delete(request, id):
    if request.method == 'POST':
        pi = FunctionUser.objects.get(pk=id)
        pi.delete()
        messages.error(request, 'profile deleted successfully.')
    return redirect(f_add)


def f_update(request, id):
    if request.method == 'POST':
        pi = FunctionUser.objects.get(pk=id)
        fm = FunctionStd(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Profile details updated.')
        return redirect(f_add)
    else:
        pi = FunctionUser.objects.get(pk=id)
    fm = FunctionStd(instance=pi)
    return render(request, 'f_update.html', {'form': fm})

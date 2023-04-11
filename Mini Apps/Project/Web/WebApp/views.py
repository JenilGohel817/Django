from operator import ge
from re import S
from django.shortcuts import render
from .models import ContactModal
from .forms import ContectForm
# Create your views here.


def Index(request):
    if request.method == 'POST':
        form = ContectForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            photo = form.cleaned_data['photo']
            gender = form.cleaned_data['gender']
            RegForm = ContactModal(name=name, photo=photo, gender=gender)
            RegForm.save()
            form = ContectForm()
    else:
        form = ContectForm()
    i = ContactModal.objects.all()
    context = {'form': form, 'i': i}
    return render(request, 'inde.html', context)


def update(request, id):
    if request.method == 'POST':
        fetch = ContactModal.objects.get(pk=id)
        form = ContectForm(request.POST, request.FILES, instance=fetch)
        if form.is_valid():
            form.save()
        return render(request, 'x.html')
    else:
        fetch = ContactModal.objects.get(pk=id)
    form = ContectForm(instance=fetch)
    return render(request, 'inde.html', {'form': form})


def delete(request, id):
    if request.method == 'GET':
        s = ContactModal.objects.get(pk=id)
        s.delete()
    return render(request, 'x.html')


def Indexx(request):
    return render(request, 'x.html')

from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import ClassStd
from .models import ClassUser
from django.contrib import messages
from django.views.generic.base import TemplateView, RedirectView
from django.views import View


# Create your views here.
class c_add(TemplateView):
    template_name = 'c_add.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = ClassStd()
        stud = ClassUser.objects.all()
        context = {'stu': stud, 'form': fm}
        return context

    def post(self, request):
        fm = ClassStd(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            stg = fm.cleaned_data['gender']
            check = ClassUser.objects.filter(name=nm).exists()
            if check:
                messages.success(request, 'User Name already exists !')
                return redirect('c_add')
            reg = ClassUser(name=nm, email=em, password=pw, gender=stg)
            reg.save()
            messages.success(request, 'profile added successfully.')
        return redirect('c_add')


class c_update(View):
    template_name = 'c_update.html'

    def get(self, request, id):
        pi = ClassUser.objects.get(pk=id)
        fm = ClassStd(instance=pi)
        return render(request, 'c_update.html', {'form': fm})

    def post(self, request, id):
        pi = ClassUser.objects.get(pk=id)
        fm = ClassStd(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Profile details updated.')
            return redirect('c_add')
        return render(request, 'c_update.html', {'form': fm})


class c_delete(RedirectView):
    url = '/class'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        messages.error(self.request, 'profile deleted successfully.')
        ClassUser.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


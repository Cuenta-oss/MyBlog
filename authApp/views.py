from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import userRegisterForm, loginUserForm
# Create your views here.


""" def registro_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
    else:
        form = UserCreationForm()
        for msg in form.error_messages():
            messages.error(request, form.error_messages[msg])
    return render(request, 'authentication.html', {'form': form})
 """


class registro_user(View):
    def get(self, request):
        form = userRegisterForm()
        context = {
            'form': form
        }
        return render(request, 'authentication.html', context)

    def post(self, request):
        form = userRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
        return render(request, 'authentication.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('home')


def log_in(request):
    if request.method == 'POST':
        form = loginUserForm(request, data=request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("username")
            pass_user = form.cleaned_data.get('password')
            user = authenticate(username=name_user, password=pass_user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                for msg in form.error_messages:
                    messages.error(request, form.error_messages[msg])
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
    form = loginUserForm()
    return render(request, 'log_in.html', {'form': form})

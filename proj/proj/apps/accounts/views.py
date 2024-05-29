from django.shortcuts import render, redirect
from .forms import CustomAuthernticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthernticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('projects:home')
    else:
        form = CustomAuthernticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('projects:home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


# Create your views here.

def logout_view(request):
    print(request)
    logout(request)
    return redirect('authorized_user:login')


def login_view(request):
    error_message = None
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if username is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('fitness_analyser:list')

        else:
            error_message = 'Something went wrong'

    context = {
        'form': form,
        'error_message': error_message
    }

    return render(request,'authorized_user/login.html',context)
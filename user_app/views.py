from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegisterUserForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('employee_list')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ('Logged in succesfully'))
                return redirect('employee_list')
            else:
                messages.success(request, ("There Was An Error Logging In, Try Again..."))
                return redirect('login_user')


    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('employee_list')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('employee_list')
    else:
        form = RegisterUserForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
                login(request, user)
                messages.success(request, ("Registration Successful!"))
                return redirect('employee_list')
        else:
            form = RegisterUserForm()

    return render(request, 'user_register.html', {
        'form': form,
    })






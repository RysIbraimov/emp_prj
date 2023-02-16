from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserForm, UserLoginForm
from .models import User

class UserRegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_register.html'
    success_url = reverse_lazy('employee_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return response

def login_user(request):
    form = UserLoginForm
    if request.user.is_authenticated:
        return redirect('employee_list')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('employee_list')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'form':form}
    return render(request, 'registration/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('employee_list')


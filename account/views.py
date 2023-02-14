from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView,DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import reverse

from .models import Employee
from .forms import EmployeeForm

# class EmployeeCreateView(CreateView):
#     model = Employee
#     form_class = EmployeeForm
#     template_name = 'employee_create.html'
#     context_object_name = 'employees'
#     success_url = reverse_lazy('employee_list')
class EmployeeCreateView(View):
    form = EmployeeForm
    template_name = 'employee_create.html'
    success_url = 'employee_list'

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(self.success_url))
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

class EmployeeList(ListView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_list.html'
    context_object_name = 'employees'

class EmployeeDetail(DetailView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_detail.html'
    context_object_name = 'employee'

# def create_user(request):
#     name = request.POST.get('name')
#     education = request.POST.get('education')
#     location = request.POST.get('location')
#     age = request.POST.get('age')
#     job = request.POST.get('job')
#
#     if request.method == 'POST':
#         try:
#             emp = Employee.objects.create(name=name,education=education,location=location,
#                                           age=age,job=job)
#             return HttpResponseRedirect(reverse('users_list'))
#         except Exception as e:
#             context = {'error':f"Не удаетсe создать пользователя {e} "}
#             return render(request, context)








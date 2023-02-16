from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView,UpdateView

from .forms import EmployeeForm
from .models import Employee


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_create.html'
    context_object_name = 'employees'
    success_url = reverse_lazy('employee_list')


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


class EmployeeDelete(DeleteView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee_list')


class EmployeeUpdate(UpdateView):
    model = Employee
    # fields = '__all__'
    form_class = EmployeeForm
    template_name = 'employee_update.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee_list')

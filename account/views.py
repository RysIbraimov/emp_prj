from django.http import FileResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,DeleteView

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

    # def render_to_response(self, context, **kwargs):
    #     return FileResponse(self.object.main_image)

class EmployeeDelete(DeleteView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee_list')










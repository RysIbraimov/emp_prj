from django.contrib import admin
from django.urls import path


from account import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.EmployeeList.as_view(), name='employee_list'),
    path('create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    # path('create/', views.create_user,name='employee_create' ),
    path('list/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),

]


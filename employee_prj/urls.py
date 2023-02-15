from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from account import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.EmployeeList.as_view(), name='employee_list'),
    path('create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('delete/<int:pk>/', views.EmployeeDelete.as_view(), name='employee_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


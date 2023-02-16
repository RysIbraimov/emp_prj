from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from account import views
from user_app import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('user/',include('django.contrib.auth.urls')),
    path('register/', user_views.UserRegisterView.as_view(), name='user_register'),
    path('login/', user_views.login_user, name='login_user' ),
    path('logout/', user_views.logout_user, name='logout_user' ),

    path('', views.EmployeeList.as_view(), name='employee_list'),
    path('create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('delete/<int:pk>/', views.EmployeeDelete.as_view(), name='employee_delete'),
    path('update/<int:pk>/', views.EmployeeUpdate.as_view(), name='employee_update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from account import views
from user_app import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', user_views.register_user, name='user_register'),
    path('login/', user_views.login_user, name='login_user' ),
    path('logout/', user_views.logout_user, name='logout_user' ),

    path('', views.EmployeeList.as_view(), name='employee_list'),
    path('create/', login_required(views.EmployeeCreateView.as_view()), name='employee_create'),
    path('<int:pk>/', login_required(views.EmployeeDetail.as_view()), name='employee_detail'),
    path('delete/<int:pk>/', login_required(views.EmployeeDelete.as_view()), name='employee_delete'),
    path('update/<int:pk>/', login_required(views.EmployeeUpdate.as_view()), name='employee_update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


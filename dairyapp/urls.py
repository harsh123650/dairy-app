
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('worker_dashboard/', views.worker_dashboard, name='worker_dashboard'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('create_user/', views.create_user_view, name='create_user'),
]

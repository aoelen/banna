from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import user_passes_test

def has_dashboard_permission(user):
    return user.groups.filter(name='factory').exists() or user.groups.filter(name='government').exists()

urlpatterns = [
    path('login', user_passes_test(has_dashboard_permission)(auth_views.login), {'template_name': 'dashboard/login.html'}, name='login'),
    path('logout', auth_views.logout, {'template_name': 'dashboard/logout.html'},  name='logout'),
    path('', user_passes_test(has_dashboard_permission)(views.dashboard), name='dashboard'),
    path('add_farmer', user_passes_test(has_dashboard_permission)(views.add_farmer), name='add_farmer'),
    path('add_user', user_passes_test(has_dashboard_permission)(views.add_user), name='add_user'),
    path('edit_farmer', user_passes_test(has_dashboard_permission)(views.edit_farmer), name='edit_farmer'),
    path('factory_data', user_passes_test(has_dashboard_permission)(views.factory_data), name='factory_data'),
    path('factory_data_delete/<int:data_id>', user_passes_test(has_dashboard_permission)(views.factory_data_delete), name='factory_data_delete'),
    path('factory_data_edit/<int:data_id>', user_passes_test(has_dashboard_permission)(views.factory_data_edit), name='factory_data_edit'),
    path('factory_overview', user_passes_test(has_dashboard_permission)(views.factory_overview), name='factory_overview'),
    path('factory', user_passes_test(has_dashboard_permission)(views.factory), name='factory'),
    path('farmers', user_passes_test(has_dashboard_permission)(views.farmers), name='farmers'),
    path('harvests', user_passes_test(has_dashboard_permission)(views.harvests), name='harvests'),
    path('trees', user_passes_test(has_dashboard_permission)(views.trees), name='trees'),
]

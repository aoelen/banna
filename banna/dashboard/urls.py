from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('index', views.index, name='index'),
    #path('login', views.login, name='login'),
    path('login', auth_views.login, {'template_name': 'dashboard/login.html'}, name='login'),
    path('logout', auth_views.logout, {'template_name': 'dashboard/logout.html'},  name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_farmer', views.add_farmer, name='add_farmer'),
    path('add_user', views.add_user, name='add_user'),
    path('edit_farmer', views.edit_farmer, name='edit_farmer'),
    path('factory_data', views.factory_data, name='factory_data'),
    path('factory_overview', views.factory_overview, name='factory_overview'),
    path('factory', views.factory, name='factory'),
    path('farmers', views.farmers, name='farmers'),
    path('harvests', views.harvests, name='harvests'),
    path('trees', views.trees, name='trees'),
    path('users', views.users, name='users'),
]

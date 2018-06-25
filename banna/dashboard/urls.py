from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('index', views.index, name='index'),
    #path('login', views.login, name='login'),
    #path('login', auth_views.login, {'template_name': 'dashboard/login.html'}, name='login'),
    #path('logout', auth_views.logout, {'template_name': 'dashboard/logout.html'},  name='logout'),
]

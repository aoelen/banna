from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

# urlpatterns = [
#     path('hallo',  views.select_month, name='select_month'),
# ]


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^overview/$', views.overview_month, name='overview_month'),
    url(r'^select_month/$', views.select_month, name='select_month'),
    #url('form_planted/$', views.form_planted, name='form_planted'),
    url('form_harvest/$', views.form_harvest, name='form_harvest'),
    url('form_fertilizer/$', views.form_fertilizer, name='form_fertilizer'),
    url('login/$', auth_views.login, {'template_name': 'farmer/registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    # # HARVEST URLS
    # url(r'^harvest/add/$', views.add_harvest, name='add_harvest'),
    # url(r'^harvest/(?P<id>\d+)/edit/$', views.edit_harvest, name='edit_harvest'),

    # url(r'^(?P<year>[0-9]{4})/(?P<month.name>[0-9]{2})/$', views.select_month, name='select_month'),
    url(r'^(?P<farm_id>[\w\-]+)/(?P<year>[\w\-]+)/(?P<month>[\w\-]+)/$', views.select_month, name='select_month'),

    path('form_planted/<int:report_id>', views.form_planted, name='form_planted'),
]

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

# urlpatterns = [
#     path('hallo',  views.select_month, name='select_month'),
# ]


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('login/$', auth_views.login, {'template_name': 'farmer/registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^farms/$', views.overview_farm, name='overview_farm'),
    url(r'^(?P<farm_id>[\w\-]+)/$', views.overview_months, name='overview_months'),
    url(r'^(?P<farm_id>[\w\-]+)/(?P<year>[\w\-]+)/(?P<month_id>[\w\-]+)/(?P<month>[\w\-]+)/$', views.overview_report, name='overview_report'),

    url('form_planted/$', views.form_planted, name='form_planted'),
    url('form_harvest/$', views.form_harvest, name='form_harvest'),
    url('form_fertilizer/$', views.form_fertilizer, name='form_fertilizer'),
]

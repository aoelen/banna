from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

# urlpatterns = [
#     path('hallo',  views.select_month, name='select_month'),
# ]


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', auth_views.login, {'template_name': 'farmer/registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/farmer/'}, name='logout'),

    #overview sections
    url(r'^farms/$', login_required(views.overview_farm), name='overview_farm'),
    url(r'^(?P<farm_id>[\w\-]+)/$', login_required(views.overview_months), name='overview_months'),
    url(r'^(?P<farm_id>[\w\-]+)/(?P<year>[\w\-]+)/(?P<month_id>[\w\-]+)/(?P<month>[\w\-]+)/$', login_required(views.overview_report), name='overview_report'),
    url(r'^(?P<farm_id>[\w\-]+)/(?P<year>[\w\-]+)/(?P<month>[\w\-]+)/$', login_required(views.overview_report), name='overview_report'),


    #forms
    url('form_planted/$', login_required(views.form_planted), name='form_planted'),
    url('form_harvest/$', login_required(views.form_harvest), name='form_harvest'),
    url('form_fertilizer/$', login_required(views.form_fertilizer), name='form_fertilizer'),

    path('form_planted/<int:report_id>', login_required(views.form_planted), name='form_planted'),
    path('form_harvest/<int:report_id>', login_required(views.form_harvest), name='form_harvest'),
    path('form_fertilizer/<int:report_id>', login_required(views.form_fertilizer), name='form_fertilizer'),
    path('success/<int:report_id>', login_required(views.success), name='success'),
]

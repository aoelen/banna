from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from . import views

# urlpatterns = [
#     path('hallo',  views.select_month, name='select_month'),
# ]


def is_farmer(user):
    return user.groups.filter(name='farmer').exists()


urlpatterns = [
    #url(r'^$', views.index, name='index'),

    #overview sections
    url(r'^farms/$', user_passes_test(is_farmer)(views.overview_farm), name='overview_farm'),
    url(r'^(?P<farm_id>[\w\-]+)/$', user_passes_test(is_farmer)(views.overview_months), name='overview_months'),
    url(r'^(?P<farm_id>[\w\-]+)/(?P<year>[\w\-]+)/(?P<month>[\w\-]+)/$', user_passes_test(is_farmer)(views.overview_report), name='overview_report'),
    # url(r'^(?P<farm_id>[\w\-]+)/(?P<year>[\w\-]+)/(?P<month>[\w\-]+)/$', login_required(views.overview_report), name='overview_report'),

    #redirect
    path('login_redirect', user_passes_test(is_farmer)(views.login_redirect), name='login_redirect'),
    #forms
    url('form_planted/$', user_passes_test(is_farmer)(views.form_planted), name='form_planted'),
    url('form_harvest/$', user_passes_test(is_farmer)(views.form_harvest), name='form_harvest'),
    url('form_fertilizer/$', user_passes_test(is_farmer)(views.form_fertilizer), name='form_fertilizer'),

    path('form_planted/<int:report_id>', user_passes_test(is_farmer)(views.form_planted), name='form_planted'),
    path('form_harvest/<int:report_id>', user_passes_test(is_farmer)(views.form_harvest), name='form_harvest'),
    path('form_fertilizer/<int:report_id>', user_passes_test(is_farmer)(views.form_fertilizer), name='form_fertilizer'),
    path('success/<int:report_id>', user_passes_test(is_farmer)(views.success), name='success'),
]

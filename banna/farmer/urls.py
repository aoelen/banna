from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.conf.urls.static import static

from . import views

def is_farmer(user):
    return user.groups.filter(name='farmer').exists()


urlpatterns = [
    #redirect
    path('login_redirect', views.login_redirect, name='login_redirect'),
    url(r'^language/$', login_required(views.choose_language), name='choose_language'),

    #overview sections
    url(r'^(?P<language_code>[\w\-]+)/farms/$', login_required(views.overview_farm), name='overview_farm'),
    url(r'^(?P<language_code>[\w\-]+)/(?P<farm_id>[\w\-]+)/$', login_required(views.overview_months), name='overview_months'),
    url(r'^(?P<language_code>[\w\-]+)/(?P<farm_id>[\w\-]+)/(?P<year>[\w\-]+)/(?P<month>[\w\-]+)/$',
        login_required(views.overview_report),
        name='overview_report'),

    #forms
    url(r'^(?P<language_code>[\w\-]+)/(?P<farm_id>[\w\-]+)/(?P<year>[\w\-]+)/(?P<month>[\w\-]+)/(?P<report_id>[\w\-]+)/plantedform/$',
        login_required(views.form_planted),
        name='form_planted'),

    url(r'^(?P<language_code>[\w\-]+)/(?P<farm_id>[\w\-]+)/(?P<year>[\w\-]+)/(?P<month>[\w\-]+)/(?P<report_id>[\w\-]+)/harvestedtreesform/$',
        login_required(views.form_harvest_trees),
        name='form_harvest_trees'),

    url(r'^(?P<language_code>[\w\-]+)/(?P<farm_id>[\w\-]+)/(?P<year>[\w\-]+)/(?P<month>[\w\-]+)/(?P<report_id>[\w\-]+)/harvestedbananasform/$',
        login_required(views.form_harvest_bananas),
        name='form_harvest_bananas'),


    url(r'^(?P<language_code>[\w\-]+)/(?P<farm_id>[\w\-]+)/(?P<year>[\w\-]+)/(?P<month>[\w\-]+)/(?P<report_id>[\w\-]+)/fertilizerform/$',
        login_required(views.form_fertilizer),
        name='form_fertilizer'),

    #form succeed
    url(r'^(?P<language_code>[\w\-]+)/(?P<farm_id>[\w\-]+)/(?P<year>[\w\-]+)/(?P<month>[\w\-]+)/(?P<report_id>[\w\-]+)/succes/$',
        login_required(views.success),
        name='success'),

    #statistics page
    url(r'^(?P<language_code>[\w\-]+)/(?P<farm_id>[\w\-]+)/statistics/$',
        login_required(views.statistics),
        name='statistics'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

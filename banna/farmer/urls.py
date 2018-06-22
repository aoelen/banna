from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index')
# ]


from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^overview/$', views.overview, name='overview'),
    url(r'^select_month/$', views.select_month, name='select_month'),
    url('form_planted/$', views.form_planted, name='form_planted'),
    url('form_harvest/$', views.form_harvest, name='form_harvest'),
    url('form_fertilizer/$', views.form_fertilizer, name='form_fertilizer'),
    url('login/$', views.login, name='login'),

    # HARVEST URLS
    url(r'^harvest/add/$', views.add_harvest, name='add_harvest'),
    url(r'^harvest/(?P<id>\d+)/edit/$', views.edit_harvest, name='edit_harvest'),

]

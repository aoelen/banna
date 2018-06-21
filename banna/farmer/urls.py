from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index')
# ]


from django.conf.urls import url, include

urlpatterns = [
    path('', views.index, name='index'),
    path('overview', views.overview, name='overview'),
    path('select_month', views.select_month, name='select_month'),
    path('form_planted', views.form_planted, name='form_planted'),
    path('form_harvest', views.form_harvest, name='form_harvest'),
    path('form_fertilizer', views.form_fertilizer, name='form_fertilizer'),
    path('login', views.login, name='login')
]

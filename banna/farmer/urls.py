from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index')
# ]


from django.conf.urls import url, include

urlpatterns = [
    # url('', views.index, name='index'),
    # YIELD URLS
    url(r'^yield/add/$', views.add_yield, name='add_yield'),
    url(r'^yield/(?P<id>\d+)/edit/$', views.edit_yield, name='edit_yield'),
    # url(r'^yield/(?P<id>\d+)/delete/$', views.delete_area, name='delete_area'),

    # HARVEST URLS
    url(r'^harvest/add/$', views.add_harvest, name='add_harvest'),
    url(r'^harvest/(?P<id>\d+)/edit/$', views.edit_harvest, name='edit_harvest'),
    # url(r'^harvest/(?P<id>\d+)/delete/$', views.delete_harvest, name='delete_harvest'),

    # FERTILIZER URLS
    url(r'^fertilizer/add/$', views.add_fertilizer, name='add_fertilizer'),
    url(r'^fertilizer/(?P<id>\d+)edit/$', views.edit_fertilizer, name='edit_fertilizer'),
    # url(r'^fertilizer/(?P<id>\d+)/delete/$', views.delete_fertilizer, name='delete_fertilizer'),

]


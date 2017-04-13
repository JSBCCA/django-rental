from django.conf.urls import url
from . import views

app_name = 'django_rental'

# Each of the urls for the page.
urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^rent/$', views.rent, name='rent'),
    url(r'^rented/(?P<id>[0-9]+)/$', views.rented, name='rented'),
    url(r'^returned/(?P<id>[0-9]+)/$', views.returned, name='returned'),
]

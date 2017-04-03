from django.conf.urls import url
from . import views

app_name = 'django_rental'

urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^rent/$', views.rent, name='rent'),
]

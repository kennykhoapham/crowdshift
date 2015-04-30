from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^(?P<year>\d{4})/(?P<make>[a-zA-Z]+)/(?P<model>[a-zA-Z]+)/', views.vehicle),
]
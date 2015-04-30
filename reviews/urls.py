from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^(\d{4})/([a-zA-Z]+)/([a-zA-Z]+)/', views.vehicle),
]
from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'reviews.views.index'),
    url(r'^reviews/', include('reviews.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search', 'reviews.views.search', name='search'),
    url(r'^result', 'reviews.views.search', name='search'),
    url(r'^write-review/(?P<year>\d{4})/(?P<make>[a-zA-Z]+)/(?P<model>[a-zA-Z]+)', 'reviews.views.write_review'),
    url(r'^add-vehicle', 'reviews.views.add_vehicle'),
)

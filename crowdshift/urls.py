from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'crowdshift.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^reviews/', include('reviews.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

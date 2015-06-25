from django.conf.urls import patterns, include, url
from django.contrib import admin

from stream import urls as stream_urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^stream', include(stream_urls)),
)

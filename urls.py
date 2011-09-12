from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'testbed.views.home', name='home'),
    url(r'^labels/', include('testbed.labels.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {'template':'home.html'} )
)

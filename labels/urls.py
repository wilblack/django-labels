from django.conf.urls.defaults import patterns, include, url
from labels.forms import TagForm, TagFormPreview
from labels.models import Tag

from django import forms

from django.views.generic.create_update import create_object, delete_object, update_object

from django.views.generic.list_detail import object_list



urlpatterns = patterns('',
    
    (r'new/$', create_object, {'form_class': TagForm} ),
    (r'edit/(?P<object_id>\d+)/$', update_object, {'form_class': TagForm} ),
    (r'delete/(?P<object_id>\d+)/$', delete_object, {'model': Tag, 'post_delete_redirect':'/labels/list/'} ),
    
    (r'post/$', TagFormPreview(TagForm)),
    (r'list/$', object_list, {'queryset': Tag.objects.all()}),
    url(r'print/(?P<tag_id>\d+)/$', 'labels.views.print_pdf'),
    (r'$', object_list, {'queryset': Tag.objects.all()}),
    
    # url(r'^$', 'testbed.views.home', name='home'),
    # url(r'^testbed/labels', include('testbed.labels.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)



from django.conf.urls.defaults import patterns, include, url
from labels.forms import TagForm
from labels.models import Tag

from django import forms

from django.views.generic.create_update import delete_object, update_object

from django.views.generic.list_detail import object_list



urlpatterns = patterns('',
    
    #(r'new/$', create_object, {'model': Tag} ),
    url(r'new/$', 'labels.views.new' ),
    
    (r'edit/(?P<object_id>\d+)/?$', update_object, {'form_class': TagForm} ),
    (r'delete/(?P<object_id>\d+)/?$', delete_object, {'model': Tag, 'post_delete_redirect':'/labels/list/'} ),
    
    (r'list/$', object_list, {'queryset': Tag.objects.all()}),
    url(r'print/(?P<tag_id>\d+)/$', 'labels.views.print_pdf'),
    (r'$', object_list, {'queryset': Tag.objects.all()}),
       
)



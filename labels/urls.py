from django.conf.urls import patterns, include, url
from labels.forms import TagForm
from labels.models import Tag

from django import forms


from labels import views as views



urlpatterns = [
    url(r'new/$', views.new),

    url(r'edit/(?P<pk>\d+)/?$', views.ListUpdate.as_view() ),
    url(r'delete/(?P<pk>\d+)/?$', views.ObjDelete.as_view() ),

    url(r'print/(?P<tag_id>\d+)/(?P<type>\w+)/$', views.print_pdf),
    url(r'^$', views.list.as_view(), name= "home")
]

from django.forms import ModelForm
from django.contrib.formtools.preview import FormPreview
from labels.models import Tag
from django.http import HttpResponseRedirect, HttpResponse


class TagForm(ModelForm):
        
    class Meta:
        model = Tag
        

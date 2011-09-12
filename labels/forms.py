from django.forms import ModelForm
from django.contrib.formtools.preview import FormPreview
from labels.models import Tag
from django.http import HttpResponseRedirect


class TagForm(ModelForm):
    class Meta:
        model = Tag
        
class TagFormPreview(FormPreview):
    def done(self, request, cleaned_data):
        tag = Tag(**cleaned_data)
        tag.save()        
        return HttpResponseRedirect('/labels/list/')
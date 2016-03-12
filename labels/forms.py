from django.forms import ModelForm
from labels.models import Tag
from formtools.preview import FormPreview
from django.http import HttpResponseRedirect, HttpResponse


class TagForm(ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'

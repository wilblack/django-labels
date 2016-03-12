# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from labels.models import Tag
from labels.forms import TagForm
from django.template import RequestContext

from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy


#show all the tags
class list(ListView):
    model = Tag

#Delete an object tag
class ObjDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('home')

#update a object
class ListUpdate(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'labels/tag_form.html'
    success_url = reverse_lazy('home')

def new(request):
    if request.method == 'POST':
        form = TagForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect('/labels/edit/%s' %instance.id)

    else:
       form = TagForm()

    return render_to_response('labels/tag_form.html', {'form':form},context_instance=RequestContext(request) )

def print_pdf(request, tag_id, type):
    from reportlab.pdfgen.canvas import Canvas
    from labels.pdf_templates import LabelPDF
    #Letter is a paper format, you can import A4 for example
    from reportlab.lib.pagesizes import letter

    tag = get_object_or_404(Tag, pk=tag_id)

    #name of the pdf
    fname = "mylabels.pdf"
    #Generating response for file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' %(fname)

    #creating the canvas object. You can change "letter" with another paper type
    c  = Canvas(response, pagesize=letter)
    #LabelPDF is the class in pdf_templates that draws on the pdf
    pdf = LabelPDF(tag,type)
    #pdf.showBoundary=1  # Turns this on for debugging purposes.
    c = pdf.draw_frames(c)

    c.save()

    return response

    tv = {'tag_id':tag_id}
    return render_to_response("labels/print.html",tv)

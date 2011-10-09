# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from labels.models import Tag
from labels.forms import TagForm
from django.template import RequestContext

from django.http import HttpResponse, HttpResponseRedirect


def new(request):
    if request.method == 'POST':
        form = TagForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect('/labels/edit/%s' %instance.id)

    else:
       form = TagForm()

    return render_to_response('labels/tag_form.html', {'form':form},context_instance=RequestContext(request) )

def print_pdf(request, tag_id):
    from reportlab.pdfgen.canvas import Canvas
    from labels.pdf_templates import LabelPDF
             
    tag = get_object_or_404(Tag, pk=tag_id)
  
    fname = "mylabels.pdf"
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' %(fname)
       
    c  = Canvas(response)
    pdf = LabelPDF(tag)
    pdf.showBoundary=1
    c = pdf.draw_frames(c)
    
    c.save()    
           
    return response

    tv = {'tag_id':tag_id}
    return render_to_response("labels/print.html",tv)

def ORIGINAL_print_pdf(request, tag_id):
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import Paragraph, Frame, Image
       
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']
    
    tag = get_object_or_404(Tag, pk=tag_id)
  
    fname = "mylabels.pdf"
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' %(fname)
    
    c  = Canvas(response)
    width =  8.5*inch/2; height = 11*inch/4.0
    for j in range(0,2):
        for i in range(0,4):
            x1 = j*8.5*inch/2.0; y1 = i*(11)*inch/4.0
            
            slogan = []
            slogan.append(Paragraph(tag.slogan1,styleN))
            slogan.append(Paragraph(tag.slogan2,styleN))
            
            contact =[]
            contact.append(Paragraph(tag.contact1,styleN))
            contact.append(Paragraph(tag.contact2,styleN))
            contact.append(Paragraph(tag.contact3,styleN))
            
            url=[Paragraph(tag.url,styleN)]
                                   
            qrcode=[]
            if tag.qrcode:
                qrcode.append(Image(tag.qrcode.path, 0.3*height, 0.3*height))           
            
            logo=[]
            if tag.logo:
                logo.append(Image(tag.logo.path, 0.4*height, 0.4*height))
            
            # Define frames and sizes here.
            logo_frame = Frame(x1,  y1+.5*height, .5*width, .5*height, showBoundary=0 )
            slogan_frame = Frame(x1,y1+.1*height, .5*width, .4*height, showBoundary=0)
            
            contact_frame = Frame(x1+.5*width, y1+.6*height, .5*width, .4*height, showBoundary=0)
            qrcode_frame = Frame(x1+.5*width,y1+.1*height, .5*width, .5*height, showBoundary=0)
            url_frame =  Frame(x1,y1, .5*width, .2*height, showBoundary=0) 
                                    
            contact_frame.addFromList(contact,c)
            slogan_frame.addFromList(slogan,c)
            qrcode_frame.addFromList(qrcode, c)
            url_frame.addFromList(url,c)
            logo_frame.addFromList(logo, c)
            
    c.save()    
           
    return response

    tv = {'tag_id':tag_id}
    return render_to_response("labels/print.html",tv)
    

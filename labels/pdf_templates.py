""" 
pdf_templates.py
================

Module to handle pdf templates for different printing layouts
Each template defines a 

1. DocTemplate
2. PageTemplate
3. Flowables

"""

from reportlab.platypus import Paragraph, Frame, Image
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet

class LabelPDF():
    def __init__(self, tag, type="default"):
        self.showBoundary = 0
        self.width =  8.5*inch/2 
        self.height = 11*inch/4.0
        
        self.tag = tag
        
                    
    
    def make_content(self):
        """
        This needs to be done for every label becuase frame.addFrame clears out the 
        flowables.
        """
        
        styles = getSampleStyleSheet()
        styleN = styles['Normal']
        
        self.slogan = []
        self.slogan.append(Paragraph(self.tag.slogan1,styleN))
        self.slogan.append(Paragraph(self.tag.slogan2,styleN))
            
        self.contact =[]
        self.contact.append(Paragraph(self.tag.contact1,styleN))
        self.contact.append(Paragraph(self.tag.contact2,styleN))
        self.contact.append(Paragraph(self.tag.contact3,styleN))
            
        self.url=[Paragraph(self.tag.url,styleN)]
                                   
        self.qrcode=[]
        if self.tag.qrcode:
            self.qrcode.append(Image(self.tag.qrcode.path, 0.3*self.height, 0.3*self.height))           
        
        self.logo=[]
        if self.tag.logo:
            self.logo.append(Image(self.tag.logo.path, 0.4*self.height, 0.4*self.height))

            
    def draw_frames(self, canvas, type='default'):    
        if type=='default':              
                                                
            for j in range(0,2):
                for i in range(0,4):
                    x1 = j*8.5*inch/2.0; y1 = i*(11)*inch/4.0
                    
                    # Have to remake the content for each iteration. Needs to be a better way
                    self.make_content()                    
                    
                    # Define frames and sizes here.
                    logo_frame = Frame(x1,  y1+.5*self.height, .5*self.width, .5*self.height, showBoundary=self.showBoundary )
                    slogan_frame = Frame(x1,y1+.1*self.height, .5*self.width, .4*self.height, showBoundary=self.showBoundary)
                    
                    contact_frame = Frame(x1+.5*self.width, y1+.6*self.height, .5*self.width, .4*self.height, showBoundary=self.showBoundary)
                    qrcode_frame = Frame(x1+.5*self.width,y1+.1*self.height, .5*self.width, .5*self.height, showBoundary=self.showBoundary)
                    url_frame =  Frame(x1,y1, .5*self.width, .2*self.height, showBoundary=self.showBoundary) 
                                            
                    contact_frame.addFromList(self.contact,canvas)
                    slogan_frame.addFromList(self.slogan,canvas)
                    qrcode_frame.addFromList(self.qrcode, canvas)
                    url_frame.addFromList(self.url,canvas)
                    logo_frame.addFromList(self.logo, canvas)
        
        return canvas 
                

 
 
    
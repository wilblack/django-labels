"""
pdf_templates.py
================

Module to handle pdf templates for different printing layouts
Each template defines a

1. DocTemplate
2. PageTemplate
3. Flowables

"""

"""
    Some definitions:
        -x1 and y1 are cordenates for the frames, depend on row and column
        -"showBoundary" shows a black line in the border of the frame
        -styleN is a dictionary(you can add more elements) and apply the style
            to the elements marked with this style. More info can be obtained
            from the documentation.

"""
from reportlab.platypus import Paragraph, Frame, Image
from reportlab.lib.units import inch, mm
from reportlab.lib.styles import getSampleStyleSheet

class LabelPDF():
    def __init__(self, tag, type="default"):
        self.showBoundary = 0 #show a black line in the border
        self.tag = tag
        self.type = type
        self._set_values(type)


    def make_content(self):
        """
        This needs to be done for every label becuase frame.addFrame clears out the
        flowables.
        """

        styles = getSampleStyleSheet()
        #You can apply different styles
        styleN = {"default": ParagraphStyle('default',fontName='Times-Roman',fontSize=12)}

        self.slogan = []
        self.slogan.append(Paragraph(self.tag.slogan1,styleN["default"]))
        self.slogan.append(Paragraph(self.tag.slogan2,styleN["default"]))

        self.contact =[]
        self.contact.append(Paragraph(self.tag.contact1,styleN["default"]))
        self.contact.append(Paragraph(self.tag.contact2,styleN["default"]))
        self.contact.append(Paragraph(self.tag.contact3,styleN["default"]))

        self.url=[Paragraph(self.tag.url,styleN["default"])]

        self.qrcode=[]
        if self.tag.qrcode:
            self.qrcode.append(Image(self.tag.qrcode.path, 1.0*inch, 1.0*inch))

        self.logo=[]
        if self.tag.logo:
            self.logo.append(Image(self.tag.logo.path, 0.4*self.height, 0.4*self.height))


    def draw_frames(self, canvas ):
        """
        Renders the label PDF for printing

        Keyword Arguments
        -----------------
        #. canvas - reportlab.pdfgen.canvas object
        #. type - STRING specifing the template type. This is dependant on the paper being used
            default - 2 column, 3 rows of labels
            avery5264 - 2 column, 3 rows to be used with Avery 5264 Shipping labels.

        """

        if self.type=='default':
            for j in range(0,self.nCols):
                for i in range(0,self.nRows):
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

        if self.type=='apli38':
            """
                I needed to print in a stickers paper an the layout was 3 columns 8 rows
                I just needed to text lines so I designed this one. I leave it hear
                because might be useful.
            """
            for j in range(0,self.nCols):
                for i in range(0,self.nRows):

                    x1 = j*self.width
                    y1 = i*self.height + self.margin_bottom
                    self.make_content()

                    slogan_frame = Frame(x1, y1, self.width, self.height, leftPadding=self.width/5, topPadding = self.height/3, showBoundary=self.showBoundary)

                    slogan_frame.addFromList(self.slogan,canvas)

        if self.type=='avery5264':
            for j in range(0,self.nCols):
                for i in range(0,self.nRows):


                    # Bootom left corner of each label
                    x1 = j*self.width + (j+1)*self.margin_vertical
                    y1 = i*self.height + self.margin_bottom

                    # Have to remake the content for each iteration. Needs to be a better way
                    self.make_content()

                    # Define frames and sizes here.
                    # Arguments are x,y, height, width
                    logo_frame = Frame(x1,  y1+.5*self.height, .5*self.width, .5*self.height, showBoundary=self.showBoundary )
                    slogan_frame = Frame(x1+.5*self.width, y1+.5*self.height, .5*self.width, .5*self.height, showBoundary=self.showBoundary)


                    #Goes in the lower left corner above the url
                    contact_frame = Frame(x1, y1+.12*self.height, .6*self.width, .3*self.height, showBoundary=self.showBoundary)

                    # Lower right corner above the url
                    qrcode_frame = Frame(x1+self.width - 1.3*inch , y1+.05*self.height, 1.3*inch, 1.3*inch, showBoundary=self.showBoundary)

                    # Goes across the bottom
                    url_frame =  Frame(x1,y1, self.width, .12*self.height, showBoundary=self.showBoundary)

                    contact_frame.addFromList(self.contact,canvas)
                    slogan_frame.addFromList(self.slogan,canvas)
                    qrcode_frame.addFromList(self.qrcode, canvas)
                    url_frame.addFromList(self.url,canvas)
                    logo_frame.addFromList(self.logo, canvas)

        return canvas

    def _set_values(self, type):

        if type == "default":
            self.nCols = 2
            self.nRows = 4
            self.width =  8.5*inch/self.nCols
            self.height = 11*inch/self.nRows
            self.margin_bottom = 0

        elif type == "avery5264":
            self.nCols = 2
            self.nRows = 3
            self.margin_bottom = .5*inch
            self.margin_vertical = .3*inch

            self.width =  (8.5*inch - 3*self.margin_vertical) / self.nCols
            self.height = (11*inch - 2*self.margin_bottom ) / self.nRows
            #self.width = 4.0*inch
            #self.height = 3.333*inch

        #Define properties for paper
        elif type == "apli38":
            self.nCols = 3              #Number of columns
            self.nRows = 8              #Number of rows
            self.margin_bottom = 8*mm   #Margin from bottom (in mm)
            self.margin_vertical = .0   #Left column margin

            self.width = 210*mm/self.nCols  #Width for each label, 210 is the widht of an A4
            self.height = (297*mm - 2*self.margin_bottom )/self.nRows #Height of each label 297 is the height of an A4

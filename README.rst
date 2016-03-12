Labels
======

A labeling app. This application allows user to fill out some basic information
and uplaod photos and QR-Codes to make a PDF template of labels to print in their
local printer.

This fork updated the project to work with Django 1.9
Original creator:  wilblack
Updated by: yabirgb

Templates
---------
Templates are PDF's that layout labels for printing. Labels comes with two templates. (Added one that I needed but has no all the fields)
More templates can be defined in label/pdf_templates.py by adding them to the
LabelPDF class.

default :
  Default template products a PDF that divides an 8.5 x 11 paper into two columns
  with 4 rows a of labels for a total of 8 labels per page.

avery5264 :
  A PDF template that prints 6 labels on an Avery 5264 Shipping label page.

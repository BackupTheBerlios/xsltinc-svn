#!/usr/bin/python
#

from Ft.Xml.Xslt.Processor import Processor
import Ft
from Ft.Xml.InputSource import DefaultFactory
import trace,sys


from xml.xpath import Context, Util

ancienset = Ft.Xml.Xslt.XsltContext.XsltContext.set
def mongetattr(ins,attname):
  print "Aie!"
  return None

def monset(ins,d):
  print "On défini un truc sur le contexte"
  ancienset(ins,d)
  

def monsetattr(ins,attname,val):
  print "HeHo !"

print Ft.Xml.Xslt.XsltContext.XsltContext.__dict__.keys()
Ft.Xml.Xslt.XsltContext.XsltContext.__dict__['set'] = monset
Ft.Xml.Xslt.XsltContext.XsltContext.__dict__['addDocument'] = monsetattr
Ft.Xml.Xslt.XsltContext.XsltContext.__dict__['__setattr__'] = monsetattr
print Ft.Xml.Xslt.XsltContext.XsltContext.__dict__.keys()
xsltproc = Processor()

xsltproc.appendStylesheet(DefaultFactory.fromUri("file:///home/t0rt00se/Travail/SILR3/pTrans/testset/persons_to_xhtml_list.xsl"))
html = xsltproc.run(DefaultFactory.fromUri("file:///home/t0rt00se/Travail/SILR3/pTrans/testset/persons.xml"))
print html

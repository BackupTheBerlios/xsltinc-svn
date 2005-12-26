#!/usr/bin/env python
import sys,time

from Ft.Xml.Domlette import PrettyPrint
from xsltinc.Observable import *

import xsltinc
import xsltinc.Dom
import weaving

class DemoTransformer:
  def __init__(self):
   self.source = xsltinc.NonvalidatingReader.parseStream(open("persons.xml"))
   self.transfo = xsltinc.NonvalidatingReader.parseStream(open("p2l.xsl"))
   #self.xsltproc = xsltinc.LinearProcessor()
   self.xsltproc = xsltinc.IncrementalProcessor()
   self.xsltproc.appendStylesheetNode(self.transfo)
   
   weaving.weaveContextSaving()
   
   self.runFirst()
   
  def runFirst(self):
   start = time.time()
   self.target = self.xsltproc.runNode(self.source)
   end = time.time()

  def runInc(self):
   start = time.time()
   self.target = self.xsltproc.runNode(self.source)
   end = time.time()

def main(args):
 demo = DemoTransformer()
 print '='*75
 #demo.source = xsltinc.Dom.CustomDomDocument(demo.source)
 #demo.source.appendChild(demo.source.createElement('person'))
 demo.runInc()
 print '='*75

if __name__=="__main__":
   main(sys.argv)

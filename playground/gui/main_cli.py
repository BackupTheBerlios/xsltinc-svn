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
   writer = xsltinc.Dom.CustomDomWriter()
   start = time.time()
   self.xsltproc.runNode(self.source,writer=writer)
   end = time.time()
   self.target = writer.getResult() 

  def runInc(self):
   writer = xsltinc.Dom.CustomDomWriter()
   start = time.time()
   self.xsltproc.runNode(self.source,writer=writer)
   print '='*75
   end = time.time()
   self.target = writer.getResult() 

def main(args):
 demo = DemoTransformer()
 demo.runInc()


if __name__=="__main__":
   main(sys.argv)

#!/usr/bin/env python
import sys,time

from Ft.Xml.Domlette import Print
from Ft.Xml import EMPTY_NAMESPACE

import xsltinc
import xsltinc.Dom
from demo import * 

from copy import copy

import weaving

class DemoTransformer:
  def __init__(self,source_file="persons.xml",transfo_file="persons_to_xhtml_list.xsl"):
   self.source =  xsltinc.Dom.CustomDomDocument(xsltinc.NonvalidatingReader.parseStream(open(source_file),stripElements=[(EMPTY_NAMESPACE, '*', 1)]))
   self.transfo = xsltinc.NonvalidatingReader.parseStream(open(transfo_file),stripElements=[(EMPTY_NAMESPACE, '*', 1)])
   self.xsltproc = xsltinc.IncrementalProcessor()
   self.source.setObserving(self.xsltproc)
   #self.xsltproc.set_observing(self.source)
   self.xsltproc.appendStylesheetNode(self.transfo)
   self.inctime = 100000000000
   self.ready_for_inc = False
   weaving.weaveRuleCreator()
   #weaving.weaveContextSaving()
   self.runFirst()

  def isReadyForInc(self):
   return self.ready_for_inc

  def changeSource(self,file):
   self.ready_for_inc = False

  def changeTarget(self,file):
   self.ready_for_inc = False

  def changeTransfo(self,file):
   self.ready_for_inc = False

  def runFirst(self):
   start = time.time()
   self.target = self.xsltproc.runNode(self.source)
   Print(self.target)
   end = time.time()
   self.can_run_inc = True
   self.oldtime = (end-start)* 10000
   self.ready_for_inc = True

  def runInc(self):
   start = time.time()
   self.target = self.xsltproc.runNodeInc(self.source)
   end = time.time()
   self.can_run_inc = True
   self.inctime = (end-start)* 10000

def main(args):
 if len(args) ==1:
   demo = DemoTransformer()
 elif len(args) != 3:
   print "USAGE : main.py xml_source_file xslt_stylesheet"
   sys.exit(0)
 else:
   demo = DemoTransformer(args[1],args[2])

 print "First Run : %d" % demo.oldtime
 

 fn = demo.source.getElementByLocalName("firstname")
 fn.childNodes[0].replaceData("titi")
 print fn.childNodes[0]
 demo.runInc()
 
 print "Inc Run : %d" %demo.inctime
 

if __name__=="__main__":
   main(sys.argv)

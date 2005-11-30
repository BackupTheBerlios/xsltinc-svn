#!/usr/bin/env python
import sys,time

from qt import *
from demo import * 

from xsltinc.Observable import *
import xsltinc
import xsltinc.Dom

class ObsListItem(QListViewItem,Observer):
  def __init__(self,parent,text):
    QListViewItem.__init__(self,parent,text)
    Observer.__init__(self)
    self.colorName = "blue"
    self.colors = { 1 : "black" , 2 : "yellow", 3: "blue" , 
                    4 : "green" , 5 : "purple" , 6 : "grey" , 7:"light blue" ,
                    8 : "black" , 9 : "forest green"}
    
  def paintCell(self, p, cg, column, width, align ):
    cg = QColorGroup(cg)
    cg.setColor(QColorGroup.Text, QColor(self.colorName))
    QListViewItem.paintCell(self, p, cg, column,width,align)

  def chooseColor(self,obj):
   self.colorName = self.colors[obj.nodeType]

  def update(self,obj,arg):
   #here I should update the qlistitem with the obj value
   self.chooseColor(obj)
   if obj.nodeType == 3: 
     self.setRenameEnabled(0,True)
     self.startRename(0)

class QListViewItemUpdater(Observer):
  """ used in order to link the ViewItem with its model without needing subclassing """
  def __init__(self,qlistitem):
   Observer.__init__(self)
   self.qlistitem = qlistitem

    
def QlistItemTreeFactory(qlistParent,domNode):
   """ here we build the given listitem, then we run the same
    method recursibely to build the childs."""
   text = domNode.localName
   if not text: text = domNode.nodeValue
   newItem =ObsListItem(qlistParent,text)
   newItem.setOpen(True)
   if hasattr(domNode,'add_observer'):
     domNode.add_observer(newItem)
     domNode.notify_observers(domNode)
   newItem.chooseColor(domNode)
   for node in domNode.childNodes:
        QlistItemTreeFactory(newItem,node)


class WindowUpdater(Observer):
  def __init__(self,model,window): 
    Observer.__init__(self)
    self.model = model
    self.window = window
    #self.window.ButtTransform1.connect(

  def update(self,obj,args=None):
    print "model changed %s -> %s" % (self.model.oldtime,self.model.inctime)
    self.window.TimeBar.setTotalSteps(self.model.oldtime)
    self.window.TimeBar.setProgress(self.model.inctime)
     

class DemoTransformer(Observable):
  def __init__(self):
   Observable.__init__(self)
   self.source = xsltinc.NonvalidatingReader.parseStream(open("persons.xml"))
   self.transfo = xsltinc.NonvalidatingReader.parseStream(open("persons_to_xhtml_list.xsl"))
   self.xsltproc = xsltinc.LinearProcessor()
   self.xsltproc.appendStylesheetNode(self.transfo)
   self.inctime = 0
   self.runFirst()

  def changeSource(self,file):
   self.notify_observers(self)

  def changeTarget(self,file):
   self.notify_observers(self)

  def changeTransfo(self,file):
   self.notify_observers(self)

  def runFirst(self):
   writer = xsltinc.Dom.CustomDomWriter()
   start = time.time()
   self.xsltproc.runNode(self.source,writer=writer)
   end = time.time()
   self.target = writer.getResult() 
   self.can_run_inc = True
   self.oldtime = (end-start)* 10000
   self.notify_observers(self)

  def runInc(self):
   writer = xsltinc.Dom.CustomDomWriter()
   start = time.time()
   self.xsltproc.runNode(self.source,writer=writer)
   end = time.time()
   self.target = writer.getResult() 
   self.can_run_inc = True
   self.inctime = (end-start)* 10000
   self.notify_observers(self)


def main(args):
 app=QApplication(args)
 mainWin = DemoView()
 demo = DemoTransformer()
 updater = WindowUpdater(demo,mainWin)
 demo.add_observer(updater)
 demo.runInc()
 QlistItemTreeFactory(mainWin.TransfoListView,demo.transfo)
 QlistItemTreeFactory(mainWin.SourceListView,demo.source)
 QlistItemTreeFactory(mainWin.TargetListView,demo.target)

 mainWin.show()

 app.connect(app, SIGNAL("lastWindowClosed()")
                , app
                , SLOT("quit()")
                )
 app.exec_loop()

if __name__=="__main__":
   main(sys.argv)

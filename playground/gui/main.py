#!/usr/bin/env python
import sys

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

class DemoTransformer:
  def __init__(self):
   self.source = xsltinc.NonvalidatingReader.parseStream(open("persons.xml"))
   self.transfo = xsltinc.NonvalidatingReader.parseStream(open("persons_to_xhtml_list.xsl"))
   writer = xsltinc.Dom.CustomDomWriter()
   self.xsltproc = xsltinc.LinearProcessor()
   self.xsltproc.appendStylesheetNode(self.transfo)
   self.xsltproc.runNode(self.source,writer=writer)
   self.target = writer.getResult() 

  def changeSource(self,file):
   pass

  def changeTarget(self,file):
   pass

  def changeTransfo(self,file):
   pass

def main(args):
 app=QApplication(args)
 mainWin = DemoView()
 demo = DemoTransformer()
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

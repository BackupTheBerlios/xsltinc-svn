#!/usr/bin/env python
import sys

from qt import *
from demo import * 

from xsltinc.Observable import *
import xsltinc
import xsltinc.Dom


class QListViewItemUpdater(Observer):
  """ used in order to link the ViewItem with its model without needing subclassing """
  def __init__(self,qlistitem):
   Observer.__init__(self)
   self.qlistitem = qlistitem

  def chooseColor(self,obj):
   if obj.nodeType ==1:
    self.qlistitem.setText(0,"1-%s" % self.qlistitem.text(0))
   elif obj.nodeType == 2:
    self.qlistitem.setText(0,"2-%s " % self.qlistitem.text(0))
   elif obj.nodeType == 3:
    self.qlistitem.setText(0, self.qlistitem.text(0))
   elif obj.nodeType == 4:
    self.qlistitem.setText(0,"4-%s " % self.qlistitem.text(0))
   elif obj.nodeType == 5:
    self.qlistitem.setText(0,"5-%s " % self.qlistitem.text(0))

  def update(self,obj,arg):
   #here I should update the qlistitem with the obj value
   self.chooseColor(obj)
    
def QlistItemTreeFactory(qlistParent,domNode):
   """ here we build the given listitem, then we run the same
    method recursibely to build the childs."""
   text = domNode.localName
   if not text: text = domNode.nodeValue
   newItem = QListViewItem(qlistParent,text)
   newItem.setOpen(True)
   if hasattr(domNode,'add_observer'):
     print "un qui est lié"
     domNode.add_observer(QListViewItemUpdater(newItem))
     domNode.notify_observers(domNode)
   for node in domNode.childNodes:
        QlistItemTreeFactory(newItem,node)


def main(args):
 app=QApplication(args)
 mainWin = DemoView()
 source = xsltinc.NonvalidatingReader.parseStream(open("persons.xml"))
 transfo = xsltinc.NonvalidatingReader.parseStream(open("persons_to_xhtml_list.xsl"))
 xsltproc = xsltinc.LinearProcessor()

 writer = xsltinc.Dom.CustomDomWriter()
 xsltproc.appendStylesheetNode(transfo)
 xsltproc.runNode(source,writer=writer)
 target = writer.getResult()

 QlistItemTreeFactory(mainWin.TransfoListView,transfo)
 QlistItemTreeFactory(mainWin.SourceListView,source)
 QlistItemTreeFactory(mainWin.TargetListView,target)

 mainWin.show()

 app.connect(app, SIGNAL("lastWindowClosed()")
                , app
                , SLOT("quit()")
                )
 app.exec_loop()

if __name__=="__main__":
   main(sys.argv)

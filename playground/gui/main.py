#!/usr/bin/env python
import sys,time

from qt import *
from demo import * 
from Ft.Xml.Domlette import Print
from xsltinc.Observable import *
import xsltinc
import xsltinc.Dom

import weaving

class ObsListItem(QListViewItem,Observer):
  def __init__(self,parent,model,window):
    if hasattr(model,'nodeValue') or hasattr(model,'localName'):
       text = model.nodeValue
       if not text:
        text = model.localName
    else:
       text = str(model)
    QListViewItem.__init__(self,parent,text)
    Observer.__init__(self)
    self.model = model
    self.window = window
    self.childs = []
    self.changed = False
    if hasattr(self.model,'add_observer'):
      self.model.add_observer(self)
    self.colorName = "blue"
    self.colors = { 1 : "black" , 2 : "yellow", 3: "blue" , 
                    4 : "green" , 5 : "purple" , 6 : "grey" , 7:"light blue" ,
                    8 : "black" , 9 : "forest green"}
    self.create_childs()
    self.chooseColor()
    self.setOpen(True)
    

  def changeName(self):
    """ called by the list when the user finished to edit the name"""
    self.model.deleteData(0,self.model.length)
    self.model.appendData("%s" % self.text(0))

  def change_node(self):
    print "CHANGEMENT DU NOEUD!"
    self.changed = True
    if self.model.nodeType == 3: 
      self.setRenameEnabled(0,True)
      self.startRename(0)
    self.model.notify_observers(self.model)

  def paintCell(self, p, cg, column, width, align ):
    """ customized method to change the color of listitems"""
    cg = QColorGroup(cg)
    cg.setColor(QColorGroup.Text, QColor(self.colorName))
    QListViewItem.paintCell(self, p, cg, column,width,align)

  def create_childs(self):
   for node in self.model.childNodes:
        self.childs.append(ObsListItem(self,node,self.window))

  def init_changed(self):
    self.changed = False
    for c in self.childs:
       c.init_changed()

  def chooseColor(self):
   if not self.changed and hasattr(self.model,'nodeType'):
     self.colorName = self.colors[self.model.nodeType]
   else:
     self.colorName = "red"


  def delete_node(self):
    pass

  def add_node(self):
    pass

  def update(self,obj,arg):
   #here I should update the qlistitem with the obj value
   self.chooseColor()
   self.changed = False

class ListItemMenu(QPopupMenu):
  def __init__(self):
    QPopupMenu.__init__(self)
    self.insertItem("Edit node",self.editSlot)
    self.insertItem("Add  Node",self.addSlot)
    self.insertItem("Delete Node",self.delSlot)
    self.item = None

  def display(self,item,position): #position is a QPoint
    self.item = item
    self.popup(position)
    #self.show()

  def editSlot(self):
    self.item.change_node()

  def addSlot(self):
    self.item.add_node()

  def delSlot(self):
    self.item.delete_node()

from Ft.Xml import EMPTY_NAMESPACE

class DemoTransformer(Observable):
  def __init__(self,source_file="persons.xml",transfo_file="persons_to_xhtml_list.xsl"):
   Observable.__init__(self)
   self.source =  xsltinc.Dom.CustomDomDocument(xsltinc.NonvalidatingReader.parseStream(open(source_file),stripElements=[(EMPTY_NAMESPACE, '*', 1)]))
   self.transfo = xsltinc.NonvalidatingReader.parseStream(open(transfo_file),stripElements=[(EMPTY_NAMESPACE, '*', 1)])
   self.xsltproc = xsltinc.IncrementalProcessor()
   self.xsltproc.set_observing(self.source)
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
   self.notify_observers(self)

  def changeTarget(self,file):
   self.ready_for_inc = False
   self.notify_observers(self)

  def changeTransfo(self,file):
   self.ready_for_inc = False
   self.notify_observers(self)

  def runFirst(self):
   start = time.time()
   self.target = self.xsltproc.runNode(self.source)
   Print(self.target)
   end = time.time()
   self.can_run_inc = True
   self.oldtime = (end-start)* 10000
   self.ready_for_inc = True
   self.notify_observers(self)

  def runInc(self):
   start = time.time()
   self.target = self.xsltproc.runNodeInc(self.source)
   end = time.time()
   self.can_run_inc = True
   self.inctime = (end-start)* 10000
   self.notify_observers(self)


class MainWin(DemoView,Observer):
  def __init__(self,model):
    DemoView.__init__(self)
    Observer.__init__(self)
    self.model = model
    self.model.add_observer(self)
    self.menu = ListItemMenu()
    self.ButtTransform1.connect(self.ButtTransform1,SIGNAL("clicked()"),self.model.runFirst)
    self.ButtTransform2.connect(self.ButtTransform2,SIGNAL("clicked()"),self.model.runInc)
    self.connect(self.SourceListView,SIGNAL("contextMenuRequested(QListViewItem*, const QPoint&, int)"),self.open_context_menu)
    self.connect(self.SourceListView,SIGNAL("itemRenamed(QListViewItem* , int)"),self.item_renamed)
    self.update_source_view()
    self.update_transfo_view()
    self.update(self.model,None)
  
  def open_context_menu(self,item,qpoint):
    if item :
      self.menu.display(item,qpoint)

  def item_renamed(self,item,col):
    item.changeName()

  def update(self,obj,args=None):
    print "model changed %s -> %s" % (self.model.oldtime,self.model.inctime)
    if self.model.oldtime < self.model.inctime: self.model.inctime = self.model.oldtime
    self.TimeBar.setTotalSteps(self.model.oldtime)
    self.TimeBar.setProgress(self.model.inctime)
    self.ButtTransform2.setEnabled(self.model.isReadyForInc())
    self.update_target_view()
    self.update_rules_view()

  def update_source_view(self):
    self.SourceListView.clear()
    ObsListItem(self.SourceListView,self.model.source,self)
    
  def update_target_view(self):
    self.TargetListView.clear()
    ObsListItem(self.TargetListView,self.model.target,self)
    
  def update_transfo_view(self):
    self.TransfoListView.clear()
    ObsListItem(self.TransfoListView,self.model.transfo,self)

  def update_rules_view(self):
    self.DepsListView.clear()
    if self.model.xsltproc.currentRule:
      ObsListItem(self.DepsListView,self.model.xsltproc.currentRule,self)
    

def main(args):
 app=QApplication(args)
 if len(args) ==1:
   demo = DemoTransformer()
 elif len(args) != 3:
   print "USAGE : main.py xml_source_file xslt_stylesheet"
   sys.exit(0)
 else:
   demo = DemoTransformer(args[1],args[2])
 mainWin = MainWin(demo)
 mainWin.show()

 app.connect(app, SIGNAL("lastWindowClosed()")
                , app
                , SLOT("quit()")
                )
 app.exec_loop()

if __name__=="__main__":
   main(sys.argv)

from Ft.Xml.Xslt.Processor import Processor
from ContextTree import ContextTree, ContextTreeNode
from Observable import *

class IncrementalProcessor(Processor,Observer):
    
    def __init__(self, stylesheetAltUris=None,
                 documentReader=None, implementation=None,
                 stylesheetIncPaths=None):
                 
      # Calling superclass constructor
      Processor.__init__(self, stylesheetAltUris=stylesheetAltUris, 
                         documentReader=documentReader, implementation=implementation,
                         stylesheetIncPaths=stylesheetIncPaths)
      Observer.__init__(self)
      self.changed_nodes = []
      self.contextTree = ContextTree() 

    def applyTemplates(self, context, params=None):
      Processor.applyTemplates(self, context, params=params)

    def update(self,obj,arg):
      #Called when an observed Node change and then will need re-evaluation
      print "un noeud qui a changé! !"
      self.changed_nodes.append(obj)
   
    def set_observing(self,domNode):
      """ this method make the processor "spy" the nodes for further changes"""
      if hasattr(domNode,"add_observer"):
          domNode.add_observer(self)
      else:
          print "WARNING : Cannot observe a non-observable instance."
      for c in domNode.childNodes:
        self.set_observing(c)


    def runNodeInc(self,DomNode,writer):
      if len(self.changed_nodes) == 0:
         print "Aucun noeud n'a changé dans l'arbre source : rien à faire."
         return
      print "Exécution : %s noeuds ont changés." % len(self.changed_nodes)
      self.runNode(DomNode,writer=writer)
      

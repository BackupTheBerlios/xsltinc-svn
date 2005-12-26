from Ft.Xml.Xslt.Processor import Processor
import Dom
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
      self.first_pass = True

      Observer.__init__(self)
      self.changed_nodes = []
      self.contextTree = ContextTree() 
      self.last_result = None
      self.currentRule = None

    def add_rule(self,rule):
     rule.parent = self.currentRule
     if self.currentRule:
       self.currentRule.childNodes.append(rule)
     else:
       rule.parent  = rule
     self.currentRule = rule

    def upper_node(self):
      self.currentRule = self.currentRule.parent

    def clear_rules(self):
      self.currentRule = None
   
    def applyTemplates(self, context, params=None):
      Processor.applyTemplates(self, context, params=params)

    def update(self,obj,arg):
      #Called when an observed Node change and then will need re-evaluation
      print "un noeud qui a changé! !"
      self.changed_nodes.append((obj,obj.get_first_nodetest()))
   


    def runNode(self,DomNode):
      """ classic XSLT transformation """
      writer = Dom.CustomDomWriter()
      Processor.runNode(self,DomNode,writer=writer)
      self.last_result = writer.getResult()
      self.first_pass = False
      return writer.getResult()
 
    def check_the_rules(self,DomNode,currentRule= None):
      if not currentRule : currentRule = self.currentRule
      if currentRule.match(DomNode):
         currentRule.execute(DomNode)
      else:
         for rule in currentRule.childNodes:
           self.check_the_rules(DomNode,currentRule=rule)
     

    def runNodeInc(self,DomNode):
      """ incremental XSLT transformation """
      writer = Dom.CustomDomWriter()
      if len(self.changed_nodes) == 0:
         print "Aucun noeud n'a changé dans l'arbre source : rien à faire."
         return self.last_result
      print "Exécution : %s noeuds ont changés." % len(self.changed_nodes)
      #now incremental transformation
      for n in self.changed_nodes:
         print "type of changed nodes : %s" % n[1].nodeName
         #for each changed node, we have to check all the rules..If one of them match, then We have to run all the execution tree, else, we should check the other rules
         self.check_the_rules(n[0])
      # FIXME: we should return the last generated tree but updated ;)
      self.changed_nodes = []
      return self.last_result
      
    def set_observing(self,domNode):
      """ this method make the processor "spy" the nodes for further changes"""
      if hasattr(domNode,"add_observer"):
          domNode.add_observer(self)
      else:
          print "WARNING : Cannot observe a non-observable instance."
      for c in domNode.childNodes:
        self.set_observing(c)

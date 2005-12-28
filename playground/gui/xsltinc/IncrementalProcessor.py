from Ft.Xml.Xslt.Processor import Processor
import Dom
from ContextTree import ContextTree, ContextTreeNode
from Observable import *
from Ft.Xml.Domlette import Print

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
      self.our_writer = Dom.CustomDomWriter()

    def add_rule(self,rule):
     rule.parent = self.currentRule
     if self.currentRule:
       self.currentRule.childNodes.append(rule)
     else:
       rule.parent  = rule
     self.currentRule = rule

    def replace_last_rule(self,rule):
     """ replace the last added rule with a new one. """
     # we have to replace currentRule with rule.
     #first we should change it in the parent
     del self.currentRule.parent.childNodes[-1]
     self.currentRule.parent.childNodes.append(rule)
     self.currentRule = self.currentRule.parent

    def upper_node(self):
     self.currentRule = self.currentRule.parent

    def clear_rules(self):
     self.currentRule = None
   
    def applyTemplates(self, context, params=None):
      Processor.applyTemplates(self, context, params=params)

    def update(self,obj,arg):
      #Called when an observed Node change and then will need re-evaluation
      self.changed_nodes.append(obj.get_first_nodetest())
   

    def runNode(self,DomNode):
      """ classic XSLT transformation """
      self.first_pass = True
      self.our_writer = Dom.CustomDomWriter()
      Processor.runNode(self,DomNode,writer=self.our_writer)
      self.last_result = self.our_writer.getResult()
      self.first_pass = False
      return self.our_writer.getResult()
 
    def check_the_rules(self,DomNodes,currentRule= None):
      if not currentRule : currentRule = self.currentRule
      for node in DomNodes:
        if currentRule.match(node):
           currentRule.execute(node)
      for rule in currentRule.childNodes:
        self.check_the_rules(DomNodes,currentRule=rule)
     

    def runNodeInc(self,DomNode):
      """ incremental XSLT transformation """
      self.writers = [self.our_writer]
      if len(self.changed_nodes) == 0:
         print "Aucun noeud n'a changé dans l'arbre source : rien à faire."
         return self.last_result
      print "Exécution incrémentale: %s noeuds ont changés." % len(self.changed_nodes)
      #for each changed node, we have to check all the rules..If one of them match, then We have to run all the execution tree, else, we should check the other rules
      self.check_the_rules(self.changed_nodes)
      self.changed_nodes = []
      return self.our_writer.getResult()
      
    def set_observing(self,domNode):
      """ this method make the processor "spy" the nodes for further changes"""
      if hasattr(domNode,"add_observer"):
          domNode.add_observer(self)
      else:
          print "WARNING : Cannot observe a non-observable instance."
      for c in domNode.childNodes:
        self.set_observing(c)

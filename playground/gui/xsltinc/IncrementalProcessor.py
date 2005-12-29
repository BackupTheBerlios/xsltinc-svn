from Ft.Xml.Xslt.Processor import Processor
import Dom
from ContextTree import ContextTree, ContextTreeNode
from Observable import *
from Ft.Xml.Domlette import Print

class IncrementalProcessor(Processor,Observer):
    """ This class is an XSLT processor extending the 4Xslt one. It features an
       incremental evaluation, meaning ten times best performances at least on a slightly 
       modified tree. BUT you have to keep in mind it's in an experimental status, and this 
       should not be used if you need right results.
    """
    def __init__(self, stylesheetAltUris=None,
                 documentReader=None, implementation=None,
                 stylesheetIncPaths=None):
      """ Optional constructor arguments are:
 |
 |    stylesheetAltUris: a list of alternative base URIs to use when
 |      resolving relative hrefs in xsl:import/xsl:include instructions.
 |      These URIs are only tried when the standard XSLT behavior of
 |      using the base URI of the xsl:import/include element itself
 |      fails to result in retrieval of a document.
 |
 |    documentReader: an object that will be used to parse XML source
 |      documents (not stylesheets). It defaults to
 |      Ft.Xml.Domlette.NonvalidatingReader, but it can be any object
 |      that has a parse() method that returns a DOM or Domlette tree.
 |
 |    implementation: a DOM implementation instance that will be used
 |      by the processor to create new source tree nodes, such as when
 |      generating result tree fragments or duplicating the source tree
 |      when runNode(node, preserveSrc=1) is called. Defaults to
 |      Ft.Xml.Domlette.implementation. Needs to have a
           createRootNode() method.
      """
                 
      # Calling superclass constructor
      Processor.__init__(self, stylesheetAltUris=stylesheetAltUris, 
                         documentReader=documentReader, implementation=implementation,
                         stylesheetIncPaths=stylesheetIncPaths)
      Observer.__init__(self)
      self.first_pass = True 
      self.changed_nodes = [] #the list of the changed nodes.
      self.last_result = None  #the last dom tree generated.
      self.currentRule = None  #a hierachy of reevaluation rules
      self.our_writer = Dom.CustomDomWriter() #the dom writer

    def add_rule(self,rule):
     """ add a rule in the current rule hiearchy"""
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
     """ Go up in the rule hierarchy"""
     self.currentRule = self.currentRule.parent

    def clear_rules(self):
     self.currentRule = None
   
    def add_tree(self,current):
      current.pv_deleted = True
      self.changed_nodes.append(current)
      for child in current.childNodes:
        self.add_tree(child)


    def update(self,obj,arg):
      """ Called when an observed Node change and then will need re-evaluation"""
      print "un noeud à changé"
      if obj.pv_deleted: #we should put all the deleted tree
        self.add_tree(current=obj)
      else:
        nodetest = obj.get_first_nodetest()
        if nodetest :
         self.changed_nodes.append(nodetest)
        else:
         self.changed_nodes.append(obj)
         
   

    def runNode(self,DomNode):
      """ classic XSLT transformation """
      self.first_pass = True
      self.currentRule = None
      self.our_writer = Dom.CustomDomWriter()
      Processor.runNode(self,DomNode,writer=self.our_writer)
      self.last_result = self.our_writer.getResult()
      self.first_pass = False
      return self.our_writer.getResult()

    def go_to_root_rule(self):
      """ position the processor to the root reevaluation rule"""
      while self.currentRule.parent and self.currentRule.parent != self.currentRule:
          self.currentRule = self.currentRule.parent
 
    def check_the_rules(self,DomNodes,currentRule= None):
      """ check the reevaluation rules and execute those that should be re-executed."""
      if not currentRule : currentRule = self.currentRule
      for node in DomNodes:
        if currentRule.match(node):
           currentRule.execute(node)
      for rule in currentRule.childNodes:
        self.check_the_rules(DomNodes,currentRule=rule)


    def delete_node(self,tree,node):
      for c in tree.childNodes:
        if node == c:
         tree.removeChild(node)
        self.delete_node(c,node)
     

    def runNodeInc(self,DomNode):
      """ incremental XSLT transformation """
      self.writers = [self.our_writer]
      if len(self.changed_nodes) == 0:
         print "Aucun noeud n'a changé dans l'arbre source : rien à faire."
         return self.last_result
      print "Exécution incrémentale: %s noeuds ont changés." % len(self.changed_nodes)
      print self.changed_nodes
      #for each changed node, we have to check all the rules..If one of them match, then We have to run all the execution tree, else, we should check the other rules
      self.go_to_root_rule()
      #first we look for deleted nodes..
      self.check_the_rules(self.changed_nodes)
      for c in self.changed_nodes:
         if hasattr(c,'pv_deleted') and c.pv_deleted and c.pv_last_generator:
            print "il faudrait supprimer %s" % c.pv_last_generator
            self.delete_node(self.last_result,c.pv_last_generator)
      self.changed_nodes = []
      self.last_result = self.our_writer.getResult()
      return self.last_result
      
    def set_observing(self,domNode):
      """ this method make the processor "spy" the nodes for further changes"""
      if hasattr(domNode,"add_observer"):
          domNode.add_observer(self)
      else:
          print "WARNING : Cannot observe a non-observable instance."
      for c in domNode.childNodes:
        self.set_observing(c)

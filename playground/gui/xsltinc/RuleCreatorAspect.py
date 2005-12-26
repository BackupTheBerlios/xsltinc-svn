from logilab.aspects.core import AbstractAspect
from logilab.aspects.prototypes import reassign_function_arguments
from IncrementalProcessor import ContextTreeNode
from copy import copy
from Rules import *

from ParseXPath import *

class RuleCreator(AbstractAspect):
    """
    """

    def __init__(self, pointcut):
        """
        """
        AbstractAspect.__init__(self, pointcut)
        self.depth = 0

    def before(self, wobj, context, *args, **kwargs):
        """Before method : we have to store the context.
        """       
        if hasattr(wobj,'_select'): # we have got a select attribute, then we can deduce rules.
          #this is the concerned nodetype node_test_expr(wobj._select.original)
          XsltContext = copy(args[0])
          new_rule = NodeTestRule(node_test_expr(str(wobj._select.original)))
          self.depth += 1
          processor = args[1]
          processor.add_rule(new_rule)
          print '-'*self.depth + '>' + str(new_rule)     
        
    def after(self, wobj, context, *args, **kwargs):        
        if hasattr(wobj,'_select'): 
          processor = args[1]
          self.depth -= 1
          processor.upper_node()

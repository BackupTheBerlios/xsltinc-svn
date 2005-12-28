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
        processor = args[1]
        if (processor.first_pass == True):
         if hasattr(wobj,'_select') and wobj._select: # we have got a select attribute, then we can deduce rules.
           #this is the concerned nodetype node_test_expr(wobj._select.original)
           XsltContext = copy(args[0])
           new_rule = NodeTestRule(XsltContext,wobj,processor,node_test_expr(str(wobj._select.original)))
           print node_test_expr(str(wobj._select.original))
           new_rule.targetNode =  processor.our_writer.getLastNode()
           new_rule.writer_state =  processor.our_writer.save_state()
           if (processor.our_writer.is_dependant()):
               print "AGREGATION DE REGLES"
               agreg_rule = AgregatedRule(processor.currentRule.childNodes[-1].context,wobj,processor)
               new_rule.endText = processor.our_writer._currText #in order to keep generated inter-data
               agreg_rule.add_rule(processor.currentRule.childNodes[-1])
               agreg_rule.add_rule(new_rule)
               agreg_rule.writer_state = processor.currentRule.childNodes[-1].writer_state
               agreg_rule.targetNode = processor.currentRule.childNodes[-1].targetNode
               agreg_rule.parent = processor.currentRule.childNodes[-1].parent
               processor.replace_last_rule(agreg_rule)
           else:
               processor.add_rule(new_rule)
           self.depth += 1
           print '-'*self.depth + '>' + str(id(new_rule.targetNode))     
        
    def after(self, wobj, context, *args, **kwargs):        
        processor = args[1]
        if processor.currentRule:
          processor.currentRule.endText = processor.our_writer._currText
        if (processor.first_pass == True):
         if hasattr(wobj,'_select'): 
          self.depth -= 1
          processor.upper_node()

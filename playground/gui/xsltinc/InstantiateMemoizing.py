from logilab.aspects.core import AbstractAspect
from logilab.aspects.prototypes import reassign_function_arguments
from IncrementalProcessor import ContextTreeNode
from copy import copy

class InstantiateMemoizing(AbstractAspect):
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
        XsltContext = copy(args[0])
        processor = args[1]
        self.depth += 1
        
        processor.contextTree.currentNode.appendChild(ContextTreeNode(context=XsltContext))
        processor.contextTree.currentNode = processor.contextTree.currentNode.lastChild()
        
        print '-'*self.depth + '>' + str(XsltContext)        
        
    def after(self, wobj, context, *args, **kwargs):        
        processor = args[1]
        self.depth -= 1
        if processor.contextTree.currentNode:
            processor.contextTree.currentNode = processor.contextTree.currentNode.parent

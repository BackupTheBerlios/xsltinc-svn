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
        
    def around(self, wobj, context, *args, **kwargs):
        """
        """       
        XsltContext = copy(args[0])
        processor = args[1]
        
        if (processor.first_pass == True):
          self.depth += 1
        
          processor.contextTree.currentNode.appendChild(ContextTreeNode(context=XsltContext))
          processor.contextTree.currentNode = processor.contextTree.currentNode.lastChild()
          
          #print '-'*self.depth + '>' + str(XsltContext)
          processor.contextTree.currentNode.targetNode = processor.writer.getLastNode()
          #print '-'*self.depth + '>' + str(processor.contextTree.currentNode.targetNode)
        
        met_name = context['method_name']
        wclass = context['__class__']
        ret = self._proceed(wobj, wclass, met_name, *args, **kwargs)
      
        if (processor.first_pass == True):
          self.depth -= 1
          if processor.contextTree.currentNode:
            processor.contextTree.currentNode = processor.contextTree.currentNode.parent

        return ret
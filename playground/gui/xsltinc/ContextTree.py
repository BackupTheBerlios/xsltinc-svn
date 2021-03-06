﻿class ContextTree:

  def __init__(self, rootContext=None):
    self.root = ContextTreeNode(context=rootContext)
    self.currentNode = self.root
    self.depth = 0
  
  def serialize(self, node=None):
    print "%s%s" % (' '*self.depth, node.context)
    self.depth += 1
    for i in node.childNodes:
      self.serialize(node=i)
    self.depth -= 1
    
class ContextTreeNode:
  
  def __init__(self, context=None):
    self.context = context
    self.parent = None
    self.targetNode = None
    self.childNodes = []
    
  def appendChild(self, child):
    self.childNodes.append(child)
    child.parent=self
    
  def lastChild(self):
    return self.childNodes[-1]

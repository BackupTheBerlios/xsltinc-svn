



class ReevaluationRule:
  """ the re-evaluation rules are nodes (just as in tree) """
  def __init__(self):
    self.childNodes = []
    self.parent = None
    self.nodeType = 1

  def match(self,node):
   """ return True if the given node match the rule """
   return True
  
  def execute(self,node):
   pass

class NodeTestRule(ReevaluationRule):
  def  __init__(self,name):
    ReevaluationRule.__init__(self)
    self.nodeTestName = name

  def match(self,node):
   """ return True if the given node match the rule """
   return node.get_first_nodetest().localName == self.nodeTestName

  def execute(self,node):
    print "%s" % node
  
  def __repr__(self):
    return ("Test de type de noeud : %s" % self.nodeTestName)

class CountTestRule(NodeTestRule):
  def __init__(self,nodeType,size):
    NodeTestRule.__init__(self,nodeType)
    self.size = size

  def __repr__(self):
    return ("Test de quantité dans collection %s de  %s" % (self.size,self.nodeTestName))

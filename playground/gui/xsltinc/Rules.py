



class ReevaluationRule:
  """ the re-evaluation rules are nodes (just as in tree) """
  def __init__(self,context=None,xslt = None,processor=None):
    self.childNodes = []
    self.parent = None
    self.context = context
    self.targetNode = None
    self.xsltNode = xslt
    self.processor = processor
    self.writer_state = None
    self.nodeType = 1

  def match(self,node):
   """ return True if the given node match the rule """
   return True
  
  def execute(self,node):
    pass


class NodeTestRule(ReevaluationRule):
  def  __init__(self,context,xslt,processor,name):
    ReevaluationRule.__init__(self,context,xslt,processor)
    self.nodeTestName = name

  def match(self,node):
   """ return True if the given node match the rule """
   if node.localName == self.nodeTestName:
     print (node.localName, self.nodeTestName)
   return node.localName == self.nodeTestName

  def execute(self,node):
    self.targetNode.clearChilds()
    self.processor.our_writer.restore_state(self.writer_state)
    self.processor.our_writer.startElement("pourVoir")
    self.processor.our_writer.endElement("pourVoir")
    #self.xsltNode.instantiate(self.context,self.processor)
  
  def __repr__(self):
    return ("Test de type de noeud : %s le context %s" % (self.nodeTestName, self.context))

class CountTestRule(NodeTestRule):
  def __init__(self,nodeType,size):
    NodeTestRule.__init__(self,nodeType)
    self.size = size

  def __repr__(self):
    return ("Test de quantité dans collection %s de  %s" % (self.size,self.nodeTestName))

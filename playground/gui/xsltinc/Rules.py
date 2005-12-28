



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
    self.endText = ""
    self.nodeType = 1

  def match(self,node):
   """ return True if the given node match the rule """
   return True
  
  def execute(self,node):
    pass


class AgregatedRule(ReevaluationRule):
  def  __init__(self,context,xslt,processor):
    ReevaluationRule.__init__(self,context,xslt,processor)
    self.rules = []

  def add_rule(self,rule):
    self.rules.append(rule)

  def match(self,node):
    for r in self.rules:
       if r.match(node): return True
    return False
 
  def __repr__(self):
    return "Agregated rule %s and %s" % (self.rules[0].nodeTestName,self.rules[1].nodeTestName)

  def execute(self,node):
    self.processor.our_writer.restore_state(self.writer_state) # preparing the writer.
    self.targetNode.clearChilds() #cleaning the target node
    diff = self.rules[1].endText.replace(self.rules[0].endText,'') #calculating the inter-nodes data
    self.rules[0].xsltNode.instantiate(self.context,self.processor)
    self.processor.our_writer._currText += diff # here we put back the interdata
    self.rules[1].xsltNode.instantiate(self.context,self.processor)
    self.processor.our_writer._completeTextNode() #finishing


class NodeTestRule(ReevaluationRule):
  def  __init__(self,context,xslt,processor,name):
    ReevaluationRule.__init__(self,context,xslt,processor)
    self.nodeTestName = name

  def match(self,node):
   """ return True if the given node match the rule """
   return node.localName == self.nodeTestName

  def execute(self,node):
    self.processor.our_writer.restore_state(self.writer_state)
    self.targetNode.clearChilds()
    #self.processor.our_writer._nodeStack[-1].clearChilds()
    self.xsltNode.instantiate(self.context,self.processor)
    self.processor.our_writer._completeTextNode()
  
  def __repr__(self):
    return ("Test de type de noeud : %s " % (self.nodeTestName))

class CountTestRule(NodeTestRule):
  def __init__(self,nodeType,size):
    NodeTestRule.__init__(self,nodeType)
    self.size = size

  def __repr__(self):
    return ("Test de quantité dans collection %s de  %s" % (self.size,self.nodeTestName))

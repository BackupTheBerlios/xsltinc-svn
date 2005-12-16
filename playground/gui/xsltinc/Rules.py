

class ReevaluationRule:
  """ the re-evaluation rules are nodes (just as in tree) """
  def __init__(self):
    self.childs = []

  def appendChild(self,node):
    self.childs.append(node)

  def match(self,node):
   """ return True if the given node match the rule """
   return True

  def evaluate_childs(self,node):
   for c in self.childs:
     if c.match(node):
       c.evaluate_childs(node)


class XpathTestRule(ReevaluationRule):
  def  __init__(self,XPathExpr):
    ReevaluationRule.__init__(self)
    self.XPathExpr = XPathExpr)

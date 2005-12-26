

class ReevaluationRule:
  """ the re-evaluation rules are nodes (just as in tree) """
  def __init__(self):
    pass

  def match(self,node):
   """ return True if the given node match the rule """
   return True

class XpathTestRule(ReevaluationRule):
  def  __init__(self,XPathExpr):
    ReevaluationRule.__init__(self)
    self.XPathExpr = XPathExpr


class CountTestRule(ReevaluationRule):
  def __init__(self,size);
    ReevaluationRule.__init__(self)
    self.size = size
   

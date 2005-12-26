

import Ft.Xml.XPath.XPathParserc as XPathParser
from Ft.Xml.XPath import *
import Ft.Xml.XPath.ParsedStep

parser = XPathParser.new()

def get_childs(TypeOfElements,current_object):
  result = []
  if hasattr(current_object,"__dict__"):
    childs = current_object.__dict__.keys()
    if  str(current_object.__class__).rfind(TypeOfElements) >= 0:
        result.append(current_object)
    for c in childs:
        result += get_childs(TypeOfElements,current_object.__dict__[c])
  return result
   
def node_test(tree):
  """ return the name of the predominant testnode. return "" if there is not
      and None if there is no nodetest in the expression  """
  #get the evaluation tree
  steps = get_childs("NodeTest",tree)
  if len(steps) == 0 :
   return ""
  else:
   retour = steps[0]
   if hasattr(retour,'_name'):
      return retour._name
   if hasattr(retour,'_localName'):
      return retour._localName

def node_test_expr(expr):
  """ return the name of the predominant testnode. return "" if there is not
      and None if there is no nodetest in the expression  """
  #get the evaluation tree
  tree = parser.parse(expr)
  steps = get_childs("NodeTest",tree)
  if len(steps) == 0 :
   return ""
  else:
   retour = steps[0]
   if hasattr(retour,'_name'):
      return retour._name
   if hasattr(retour,'_localName'):
      return retour._localName

def get_function(expr):
  """ return the name of the function call. return "" if there is not
      and None if there is no function call  """
  #get the evaluation tree
  tree = parser.parse(expr)
  steps = get_childs("FunctionCall",tree)
  if len(steps) == 0 :
   return ""
  else:
   retour = steps[0]
   if hasattr(retour,'_name'):
      return retour._name
   if hasattr(retour,'_localName'):
      return retour._localName

import unittest
from Ft.Xml import InputSource


class XpathParseTest(unittest.TestCase):
   def test_expressions(self):
    self.assertEqual("structure",node_test_expr("/machin/structure[1]"))

   def test_empty_nodetypes(self):
    self.assertEqual("",node_test_expr("$outputWidth"))
    self.assertEqual(None,node_test_expr("child::node()"))
    self.assertEqual(None,node_test_expr("1+count(preceding-sibling::*)"))

   def test_filled_nodetypes(self):
    self.assertEqual("teacherId",node_test_expr("//hTechEntry[@htech:idM=$idModule]/@htech:teacherId"))
    self.assertEqual("title",node_test_expr("//hTechEntry[@htech:idM=$idModule]/title"))
    self.assertEqual("biblioentry",node_test_expr("//biblioentry[abbrev=current()/descendant::citation]"))
    self.assertEqual("Book",node_test_expr("1+count(preceding-sibling::Book)"))

   def test_get_functions(self):
    self.assertEqual("position",get_function("1+position(preceding-sibling::*)"))
    self.assertEqual("count",get_function("1+count(preceding-sibling::*)"))
    self.assertNotEqual("count",get_function("child::node()"))
  
    

if __name__=="__main__":
   unittest.main()


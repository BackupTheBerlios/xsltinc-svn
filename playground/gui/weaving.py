from Ft.Xml.Xslt.StylesheetTree import XsltElement

# Template's instruction
from Ft.Xml.Xslt.TemplateElement import TemplateElement

# Controls' instructions
from Ft.Xml.Xslt.ApplyImportsElement import ApplyImportsElement
from Ft.Xml.Xslt.ApplyTemplatesElement import ApplyTemplatesElement
from Ft.Xml.Xslt.CallTemplateElement import CallTemplateElement
from Ft.Xml.Xslt.ChooseElement import ChooseElement, OtherwiseElement, WhenElement
from Ft.Xml.Xslt.SortElement import SortElement
from Ft.Xml.Xslt.IfElement import IfElement
from Ft.Xml.Xslt.ForEachElement import ForEachElement
from Ft.Xml.Xslt.WithParamElement import WithParamElement

# Productions' instructions
from Ft.Xml.Xslt.AttributeElement import AttributeElement
from Ft.Xml.Xslt.CommentElement import CommentElement
from Ft.Xml.Xslt.CopyElement import CopyElement
from Ft.Xml.Xslt.CopyOfElement import CopyOfElement
from Ft.Xml.Xslt.ElementElement import ElementElement
from Ft.Xml.Xslt.ProcessingInstructionElement import ProcessingInstructionElement
from Ft.Xml.Xslt.NumberElement import NumberElement
from Ft.Xml.Xslt.TextElement import TextElement
from Ft.Xml.Xslt.ValueOfElement import ValueOfElement

# Variables' instructions
from Ft.Xml.Xslt.ParamElement import ParamElement
from Ft.Xml.Xslt.VariableElement import VariableElement

from logilab.aspects.weaver import weaver, PointCut
from xsltinc.InstantiateMemoizing import *

def weaveContextSaving():  
  # Weaving Memoizing Aspect with XSLTElement
   
  xsltElements = [
    XsltElement,
    TemplateElement,  
    ApplyImportsElement,
    ApplyTemplatesElement,
    CallTemplateElement,
    ChooseElement,
    ForEachElement,
    IfElement,
    SortElement,
    OtherwiseElement,
    WhenElement,
    WithParamElement,
    AttributeElement,
    CommentElement,
    CopyElement,
    CopyOfElement,
    ElementElement,
    ProcessingInstructionElement,
    NumberElement,
    TextElement,
    ValueOfElement,
    ParamElement,
    VariableElement
  ]
   
  pcut = PointCut()
  for e in xsltElements: 
    pcut.add_method(e, 'instantiate')
  
  weaver.weave_pointcut(pcut, InstantiateMemoizing)
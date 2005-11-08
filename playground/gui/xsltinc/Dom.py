from Ft.Xml.Xslt.DomWriter import  DomWriter,EMPTY_NAMESPACE
import Ft.Xml.cDomlette
from Observable import *

class CustomDomElement(Observer,Observable):
  """ This class extend the cDomlette Element adding an Observable behavior.
     It is an Observer because it keep an eye on it's childs
  """
  def __init__(self,cDomElement):
    Observable.__init__(self)
    Observer.__init__(self)
    self.cdomlette = cDomElement
    self.nodeType = self.cdomlette.nodeType
    self.localName = self.cdomlette.localName
    self.nodeValue = self.cdomlette.nodeValue
    self.attributes = self.cdomlette.attributes
    self.baseURI = self.cdomlette.baseURI
    self.childNodes = Olist(self.cdomlette.childNodes)
    self.childNodes.add_observer(self)

  def update(self,obj,arg=None):
    #update from a child
    self.notify_observers(self)

  def appendChild(self,child):
    self.childNodes.append(child)
    if 'cdomlette' in child.__dict__.keys():
       self.cdomlette.appendChild(child.cdomlette)
    else:
       self.cdomlette.appendChild(child)
    self.notify_observers(self)



# FIXME : all members are  - appendChild', 'attributes', 'baseURI', 'childNodes', 'cloneNode', 'firstChild', 'getAttributeNS', 'getAttributeNodeNS', 'hasAttributeNS', 'hasChildNodes', 'insertBefore', 'isSameNode', 'lastChild', 'localName', 'namespaceURI', 'nextSibling', 'nodeName', 'nodeType', 'nodeValue', 'normalize', 'ownerDocument', 'parentNode', 'prefix', 'previousSibling', 'removeAttributeNS', 'removeAttributeNode', 'removeChild', 'replaceChild', 'rootNode', 'setAttributeNS', 'setAttributeNodeNS', 'tagName', 'xmlBase', 'xpath', 'xpathAttributes', 'xpathNamespaces'


class CustomDomDocument(CustomDomElement):
  def __init__(self,cDomDocument):
    CustomDomElement.__init__(self,cDomDocument)

  def createDocumentFragment(self):
    return CustomDomElement(self.cdomlette.createDocumentFragment())

  def createElementNS(self,a,b):
    return CustomDomElement(self.cdomlette.createElementNS(a,b))
 
  def createProcessingInstruction(self):
    return CustomDomElement(self.cdomlette.createProcessingInstruction())

  def createAttributeNS(self):
    return CustomDomElement(self.cdomlette.createAttributeNS())

  def createComment(self):
    return CustomDomElement(self.cdomlette.createComment())

  def createTextNode(self,t):
    return CustomDomElement(self.cdomlette.createTextNode(t))


class CustomDomWriter(DomWriter):
  """ This class is here in order to create special DOM instances from the parsers."""
  def __init__(self):
    DomWriter.__init__(self)
    self._root = CustomDomElement(self._root)
    self._nodeStack = [self._root]
    self._currElement = None
    self._currText = ''
    self._ownerDoc = CustomDomDocument(self._ownerDoc)


  def endElement(self, name, namespace=EMPTY_NAMESPACE):
    self._completeTextNode()
    new_element = self._nodeStack[-1]
    del self._nodeStack[-1]
    if new_element.__class__ == CustomDomElement :
       self._nodeStack[-1].appendChild((new_element))
    else:
       self._nodeStack[-1].appendChild(CustomDomElement(new_element))
    return


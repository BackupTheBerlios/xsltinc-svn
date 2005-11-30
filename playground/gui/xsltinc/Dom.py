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
    self.memoizing=  dict() #this object is used to keep objects I send back

  def __memoized__(self,name,value):
    if name in self.memoizing.keys():
      if id(self.memoizing[name][0]) == id(value):
         return self.memoizing[name][1]
    self.memoizing[name] = (value,CustomDomElement(value))
    return self.memoizing[name][1]

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

  def cloneNode(self):
     return CustomDomElement(self.cdomlette.cloneNode())

  def firstChild(self):
    return self.__memoized__("firstChild",self.cdomlette.firstChild())

  def getAttributeNS(self):
    return self.cdomlette.getAttributeNS()

  def getAttributeNodeNS(self):
    return self.cdomlette.getAttributeNodeNS()

  def hasAttributeNS(self):
    return self.cdomlette.hasAttributeNS()

  def hasChildNodes(self):
    return self.cdomlette.hasChildNodes()

  def insertBefore(self,node):
    self.cdomlette.insertBefore(node)

  def isSameNode(self,node):
    return id(self) == id(node) or id(self.cdomlette) == id(node)

 
  def lastChild(self):
    return self.__memoized__("lastChild",self.cdomlette.lastChild())

  def localName(self):
    return self.cdomlette.localName()

  def namespaceURI(self):
    return self.cdomlette.namespaceURI()

  def nextSibling(self):
    return self.__memoized__("nextSibling",self.cdomlette.nextSibling())

  def nodeName(self):
    return self.cdomlette.nodeName()

  def nodeType(self):
    return self.cdomlette.nodeType()

  def nodeValue(self):
    return self.cdomlette.nodeValue()

  def normalize(self):
    self.cdomlette.normalize()

  def ownerDocument(self):
    return self.cdomlette.ownerDocument()

  def parentNode(self):
    return CustomDomElement(self.cdomlette.nextSibling())

  def removeAttributeNS(self):
    self.cdomlette.removeAttributeNS()

  def removeAttributeNode(self,node):
    self.cdomlette.removeAttributeNode(self,node)

  def removeChild(self,child):
    self.cdomlette.removeChild(child.cdomlette)

  def replaceChild(self,child):
    self.cdomlette.replaceChild(child.cdomlette)

  def rootNode(self):
    return self.__memoized__("rootNode",self.cdomlette.rootNode())


  def setAttributeNS(self,attr,namespace):
    pass

  def setAttributeNodeNS(self,attr,namespace):
    pass

  def tagName(self):
    return self.cdomlette.tagName()

  def xmlBase(self):
    return self.cdomlette.xmlBase()

  def xpath(self,path):
    return self.cdomlette.path(path)


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


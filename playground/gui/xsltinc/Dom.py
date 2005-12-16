from Ft.Xml.Xslt.DomWriter import  DomWriter,EMPTY_NAMESPACE
import Ft.Xml.cDomlette
from Observable import *

class CustomDomElement(Observer,Observable):
  """ This class extend the cDomlette Element adding an Observable behavior.
     It is an Observer because it keep an eye on it's childs
  """
  def __init__(self,cDomElement):
    self.__wrapped_attributes = ["nodeType","tagName","localName"]
    Observable.__init__(self)
    Observer.__init__(self)
    self.pv_cdomlette= cDomElement
    self.pv_memoizing=  dict() #t
    self.sync_with_wrapped

  def __getattr__(self,attr):
    if attr.startswith('pv_') : 
      return getattr(self,attr)
    else:
      retour= getattr(self.pv_cdomlette,attr)
      #here we should check in memoized tab
      return retour

  def sync_with_wrapped(self):
    self.nodeType = self.__cdomlette.nodeType
    self.tagName = self.__cdomlette.tagName
    self.localName = self.__cdomlette.localName
    self.firstChild = self.__memoized__(self.__cdomlette.firstChild)
    self.lastChild = self.__memoized__(self__cdomlette.lastChild)
    self.xmlBase = self.__cdomlette.xmlBase
    self.nodeValue = self.__cdomlette.nodeValue
    self.attributes = self.__cdomlette.attributes
    self.baseURI = self.__cdomlette.baseURI

  def __memoized__(self,name,value):
    if name in self.pv_memoizing.keys():
      if id(self.pv_memoizing[name][0]) == id(value):
         return self.pv_memoizing[name][1]
    self.pv_memoizing[name] = (value,CustomDomElement(value))
    return self.pv_memoizing[name][1]

  def update(self,obj,arg=None):
    #update from a child
    self.notify_observers(self)

  def appendChild(self,child):
    self.childNodes.append(child)
    if 'pv_cdomlette' in dir(child):
       self.pv_cdomlette.appendChild(child.pv_cdomlette)
    else:
       self.pv_cdomlette.appendChild(child)
    self.notify_observers(self)

  def cloneNode(self):
     return CustomDomElement(self.pv_cdomlette.cloneNode())

  def getAttributeNS(self):
    return self.pv_cdomlette.getAttributeNS()

  def getAttributeNodeNS(self):
    return self.pv_cdomlette.getAttributeNodeNS()

  def hasAttributeNS(self):
    return self.pv_cdomlette.hasAttributeNS()

  def hasChildNodes(self):
    return self.pv_cdomlette.hasChildNodes()

  def insertBefore(self,node):
    self.pv_cdomlette.insertBefore(node)
    self.sync_with_wrapped

  def isSameNode(self,node):
    return id(self) == id(node) or id(self.pv_cdomlette) == id(node)


  def namespaceURI(self):
    return self.pv_cdomlette.namespaceURI()

  def nextSibling(self):
    return self.__memoized__("nextSibling",self.pv_cdomlette.nextSibling())

  def nodeName(self):
    return self.pv_cdomlette.nodeName()

  def normalize(self):
    self.pv_cdomlette.normalize()

  def ownerDocument(self):
    return self.pv_cdomlette.ownerDocument()

  def parentNode(self):
    return CustomDomElement(self.pv_cdomlette.parentNode())

  def removeAttributeNS(self):
    self.pv_cdomlette.removeAttributeNS()
    self.sync_with_wrapped

  def removeAttributeNode(self,node):
    self.pv_cdomlette.removeAttributeNode(self,node)

  def removeChild(self,child):
    self.pv_cdomlette.removeChild(child.cdomlette)
    self.sync_with_wrapped

  def replaceChild(self,child):
    self.pv_cdomlette.replaceChild(child.cdomlette)
    self.sync_with_wrapped

  def rootNode(self):
    return self.__memoized__("rootNode",self.pv_cdomlette.rootNode())


  def setAttributeNS(self,attr,namespace):
    pass

  def setAttributeNodeNS(self,attr,namespace):
    pass

  def xpath(self,path):
    return self.pv_cdomlette.path(path)


# FIXME : all members are  - appendChild', 'attributes', 'baseURI', 'childNodes', 'cloneNode', 'firstChild', 'getAttributeNS', 'getAttributeNodeNS', 'hasAttributeNS', 'hasChildNodes', 'insertBefore', 'isSameNode', 'lastChild', 'localName', 'namespaceURI', 'nextSibling', 'nodeName', 'nodeType', 'nodeValue', 'normalize', 'ownerDocument', 'parentNode', 'prefix', 'previousSibling', 'removeAttributeNS', 'removeAttributeNode', 'removeChild', 'replaceChild', 'rootNode', 'setAttributeNS', 'setAttributeNodeNS', 'tagName', 'xmlBase', 'xpath', 'xpathAttributes', 'xpathNamespaces'


class CustomDomDocument(CustomDomElement):
  def __init__(self,cDomDocument):
    CustomDomElement.__init__(self,cDomDocument)

  def createDocumentFragment(self):
    return CustomDomElement(self.pv_cdomlette.createDocumentFragment())

  def createElementNS(self,a,b):
    return CustomDomElement(self.pv_cdomlette.createElementNS(a,b))

  def createElement(self,a,b):
    return CustomDomElement(self.pv_cdomlette.createElement(a,b))
 
  def createProcessingInstruction(self):
    return CustomDomElement(self.pv_cdomlette.createProcessingInstruction())

  def createAttributeNS(self):
    return CustomDomElement(self.pv_cdomlette.createAttributeNS())

  def createComment(self):
    return CustomDomElement(self.pv_cdomlette.createComment())

  def createTextNode(self,t):
    return CustomDomElement(self.pv_cdomlette.createTextNode(t))


class CustomDomWriter(DomWriter):
  """ This class is here in order to create special DOM instances from the parsers."""
  def __init__(self):
    DomWriter.__init__(self)
    self._root = CustomDomDocument(self._root)
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

import unittest
from Ft.Xml import InputSource


class DomNodeTest(unittest.TestCase):

   def isWrapped(self,n1):
    self.assertEqual(n1.__class__,CustomDomElement)

   def NodeEqual(self,n1,n2):
    self.assertEqual(n1.tagName,n2.tagName)
    self.assertEqual(n1.nodeType,n2.nodeType)
    self.assertEqual(n1.xmlBase,n2.xmlBase)
    self.assertEqual(len(n1.childNodes),len(n2.childNodes))
    self.assertEqual(n1.firstChild,n2.firstChild)
    self.assertEqual(n1.lastChild,n2.lastChild)
    
   def testCreate(self):
    doc = Ft.Xml.cDomlette.implementation.createRootNode('file:///article.xml')
    docelement = doc.createElementNS(EMPTY_NAMESPACE, 'racine')
    sourcebis = CustomDomElement(docelement)
    self.NodeEqual(docelement,sourcebis)

   def testAppend(self):
    doc = Ft.Xml.cDomlette.implementation.createRootNode('file:///article.xml')
    docelement = doc.createElementNS(EMPTY_NAMESPACE, 'racine')
    sourcebis = CustomDomElement(docelement)
    self.NodeEqual(docelement,sourcebis)
    sourcebis.appendChild(doc.createElementNS(EMPTY_NAMESPACE, 'fils1'))
    self.NodeEqual(docelement,sourcebis)
    self.NodeEqual(docelement.firstChild,sourcebis.firstChild)
    self.NodeEqual(docelement.lastChild,sourcebis.lastChild)


if __name__=="__main__":
   unittest.main()


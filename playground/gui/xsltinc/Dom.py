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
    self.childNodes = Olist(self.pv_cdomlette.childNodes)

  def __getattr__(self,attr):
    if attr.startswith('pv_') : 
      return getattr(self,attr)
    else:
      retour= getattr(self.pv_cdomlette,attr)
      #here we should check in memoized tab
      if retour.__class__ == Ft.Xml.cDomlette.Document:
        retour = self.__memoized__(attr,retour)
      return retour

  def get_first_nodetest(self):
     # looking for the first parent having a type
     parent = self.parentNode
     while parent and parent.nodeType != 1:
       print parent.nodeType
       parent = parent.parentNode
     return parent

  def sync_with_wrapped(self):
    self.nodeType = self.__cdomlette.nodeType
    self.nodeName = self.__cdomlette.nodeName
    self.tagName = self.__cdomlette.tagName
    self.localName = self.__cdomlette.localName
    self.xmlBase = self.__cdomlette.xmlBase
    self.nodeValue = self.__cdomlette.nodeValue
    self.attributes = self.__cdomlette.attributes

  def __memoized__(self,name,value):
    if name in self.pv_memoizing.keys():
      if id(self.pv_memoizing[name][0]) == id(value):
         return self.pv_memoizing[name][1]
    if not isinstance(value,list):
      self.pv_memoizing[name] = (value,CustomDomElement(value))
    else:
      self.pv_memoizing[name] = (value,value)
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


  def nextSibling(self):
    return self.__memoized__("nextSibling",self.pv_cdomlette.nextSibling())


  def normalize(self):
    self.pv_cdomlette.normalize()

  def ownerDocument(self):
    return self.pv_cdomlette.ownerDocument()

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



  def setAttributeNS(self,attr,namespace):
    pass

  def setAttributeNodeNS(self,attr,namespace):
    pass

  def xpath(self,path):
    return self.__memoized__("xpath",self.pv_cdomlette.xpath(path))


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

class Olist(Observable):
   def __init__(self,l=[]):
    Observable.__init__(self)
    self._contenu = list(l)
    self.pv_memoizing=  dict() 
  
   def append(self,truc):
    self._contenu.append(truc)
    self.notify_observers(self)

   def remove(self,truc):
    self._contenu.remove(truc)
    self.notify_observers(self)

   def __iadd__(self,truc):
    self._contenu.__iadd__(truc)
    self.notify_observers(self)

   def __len__(self): return self._contenu.__len__()
 
   def __len__(self): return self._contenu.__len__()
   def __eq__(self): return self._contenu.__eq__()
   def __le__(self): return self._contenu.__le__()
   def __lt__(self): return self._contenu.__lt__()
   def __ge__(self): return self._contenu.__ge__()
   def __gt__(self): return self._contenu.__gt__()
   #def __iter__(self): 
   #  print "#######  ITER ############"
   #  return self.__memoized__("iter",self._contenu.__iter__())
   def __getslice__(self,i): return self._contenu.__getslice__(i)

   def __memoized__(self,name,value):
    if name in self.pv_memoizing.keys():
      if id(self.pv_memoizing[name][0]) == id(value):
         return self.pv_memoizing[name][1]
    self.pv_memoizing[name] = (value,CustomDomElement(value))
    return self.pv_memoizing[name][1]

   def __getitem__(self,i): 
     return self.__memoized__("getitem_%s" % i,self._contenu.__getitem__(i))

   def __contains__(self): return self._contenu.__contains__()

   def __delslice__(self,truc):
     self._contenu.__delslice__(truc)
     self.notify_observers(self)

   def __setitem__(self,truc):
     self._contenu.__setitem__(truc)
     self.notify_observers(self)

   def __mul__(self,truc):
     self._contenu.__mul__(truc)
     self.notify_observers(self)

   def __reduce__(self,truc):
     self._contenu.__reduce__(truc)
     self.notify_observers(self)


   def pop(self):
     retour = self._contenu.pop()
     self.notify_observers(self)
     return retour


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
    
  def getLastNode(self):
    return self._nodeStack[-1]

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


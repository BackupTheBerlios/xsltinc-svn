from Ft.Xml.Xslt.DomWriter import  DomWriter,EMPTY_NAMESPACE
import Ft.Xml.cDomlette
from Observable import *
from copy import copy

class CustomDomElement(Observable):
  """ This class extend the cDomlette Element adding an Observable behavior.
  """
  def __init__(self,cDomElement):
    Observable.__init__(self)
    self.pv_cdomlette= cDomElement # the wrapped builtin instance
    self.pv_memoizing=  dict() #used to keep track of returned generated instance.
                               #if firstChild() return an instance, it should return the same after.
    self.childNodes = Olist(self.pv_cdomlette.childNodes)
    self.pv_deleted = False
    self.pv_last_generator = None

  def __getattr__(self,attr):
    if attr.startswith('pv_') or attr == "childNodes" : 
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
       parent = parent.parentNode
     return parent

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
       #here we try to append an already wrapped node
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

  def removeAttributeNode(self,node):
    self.pv_cdomlette.removeAttributeNode(self,node)

  def clearChilds(self):
    for cchild  in self.pv_cdomlette.childNodes:
       self.pv_cdomlette.removeChild(cchild)
    self.childNodes.clear()

  def removeChild(self,child):
    self.pv_cdomlette.removeChild(child.pv_cdomlette)
    for i in range(0,len(self.childNodes)-1):
      if id(self.childNodes[i]) == id(child):
       toto = self.childNodes[i]
       toto.pv_deleted = True
       self.notify_observers(toto)
       del self.childNodes[i]
       print "coucou %s" % toto
    self.notify_observers(self)

  def replaceChild(self,child):
    self.pv_cdomlette.replaceChild(child.cdomlette)

  def replaceData(self,newdata):
   self.deleteData(0,self.length)
   self.appendData(newdata)
   self.notify_observers(self,None)

  def setAttributeNS(self,attr,namespace):
    pass

  def setAttributeNodeNS(self,attr,namespace):
    pass

  def xpath(self,path):
    return self.__memoized__("xpath",self.pv_cdomlette.xpath(path))


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

  def getElementByLocalName(self,localName, current_node=None):
    if current_node == None:
      current_node = self.rootNode
    if current_node.localName == localName:
      return current_node
    else:
      for c in current_node.childNodes:
          toto = self.getElementByLocalName(localName, c)
          if toto:
           return toto
    return None

class Olist(Observable):
   def __init__(self,l=[]):
    Observable.__init__(self)
    self._contenu = list(l)
    self.pv_memoizing=  dict() 
  
   def append(self,truc):
    self._contenu.append(truc)
    self.notify_observers(self)

   def clear(self):
    self._contenu = []
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

   def __getslice__(self,i): return self._contenu.__getslice__(i)
    
   # __iter__ is tricky to wrap and not needed, only here for performances...

   def __memoized__(self,name,value):
    if name in self.pv_memoizing.keys():
      if id(self.pv_memoizing[name][0]) == id(value):
         return self.pv_memoizing[name][1]
    self.pv_memoizing[name] = (value,CustomDomElement(value))
    return self.pv_memoizing[name][1]

   def __getitem__(self,i): 
     retour  = self._contenu.__getitem__(i)
     if 'pv_cdomlette' in dir(retour):
       return retour
     return self.__memoized__("getitem_%s" % i,self._contenu.__getitem__(i))

   def __contains__(self): return self._contenu.__contains__()

   def __delslice__(self,truc):
     self._contenu.__delslice__(truc)
     self.notify_observers(self)
  
   def __delitem__(self,item):
     self._contenu.__delitem__(item)

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

from Ft.Xml.Lib.XmlString import SplitQName

class CustomDomWriter(DomWriter):
  """ This class is here in order to create special DOM instances from the parsers."""
  def __init__(self):
    DomWriter.__init__(self)
    self._root = CustomDomDocument(self._root)
    self._nodeStack = [self._root]
    self._currElement = None
    self._currText = ''
    self._ownerDoc = CustomDomDocument(self._ownerDoc)

  def is_dependant(self):
    return self._currText != ""

  def startElement(self, name, namespace=EMPTY_NAMESPACE, extraNss=None):
     self._completeTextNode()
     new_element = self._ownerDoc.createElementNS(namespace, name)
     self._nodeStack.append(new_element)
     extraNss = extraNss or {}
     prefix, localName = SplitQName(name)
     for prefix in extraNss.keys():
         if prefix:
             new_element.setAttributeNS(XMLNS_NAMESPACE,
                                           'xmlns:'+prefix,
                                          extraNss[prefix])
         else:
             new_element.setAttributeNS(XMLNS_NAMESPACE,
                                        'xmlns',
                                        extraNss[None] or u'')
     return

  def endElement(self, name, namespace=EMPTY_NAMESPACE):
    self._completeTextNode()
    new_element = self._nodeStack[-1]
    del self._nodeStack[-1]
    self._nodeStack[-1].appendChild((new_element))
    return

  def display_tree(self,current_el=None,depth = 0):
    if current_el == None : current_el = self._root
    print str(id(current_el)) + '-'*depth + '>' +str(current_el) + "en vrai %s enfants " % len(current_el.childNodes)
    for child in current_el.childNodes:
         self.display_tree(current_el=child,depth = depth +1)

  def save_state(self):
    return (self._currElement, self._currText,copy(self._nodeStack))
    
  def restore_state(self,new_state):
    self._nodeStack = new_state[2]
    self._currElement = new_state[0]
    self._currText = new_state[1] 
    
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
  
   def testChilds(self):
    doc = Ft.Xml.cDomlette.implementation.createRootNode('file:///article.xml')
    docelement = doc.createElementNS(EMPTY_NAMESPACE, 'racine')
    sourcebis = CustomDomElement(docelement)
    self.NodeEqual(docelement,sourcebis)
    sourcebis.appendChild(doc.createElementNS(EMPTY_NAMESPACE, 'fils1'))
    sourcebis.appendChild(doc.createElementNS(EMPTY_NAMESPACE, 'fils2'))
    sourcebis.appendChild(doc.createElementNS(EMPTY_NAMESPACE, 'fils3'))
    sourcebis.appendChild(doc.createElementNS(EMPTY_NAMESPACE, 'fils4'))
    self.assertEqual(len(sourcebis.childNodes),4)
    sourcebis.clearChilds()
    self.assertEqual(len(sourcebis.childNodes),0)
    self.assertEqual(len(sourcebis.pv_cdomlette.childNodes),0)


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


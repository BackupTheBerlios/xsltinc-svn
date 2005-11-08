class Observer:
 def __init__(self):
   pass

 def update(self,obj,arg):
   pass

class Observable:
  def __init__(self):
    self.observers = []

  def add_observer(self,obs):
    self.observers.append(obs)

  def notify_observers(self,obj,arg=None):
    for  i in self.observers:
      i.update(obj,arg)

class Olist(Observable):
   """ incomplete implémentation of a shareable list"""
   def __init__(self,l=[]):
    Observable.__init__(self)
    self._contenu = list(l)
  
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
   def __iter__(self): return self._contenu.__iter__()
   def __getslice__(self,i): return self._contenu.__getslice__(i)
   def __getitem__(self,i): 
     return self.__getattr__(toto)

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



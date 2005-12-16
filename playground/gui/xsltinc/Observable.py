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



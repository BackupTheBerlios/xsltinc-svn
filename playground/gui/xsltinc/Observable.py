class Observer:
 def __init__(self):
   pass

 def update(self,obj,arg):
   """ you should redefine this method to update your view when the model change"""
   pass

class Observable:
  def __init__(self):
    self.observers = []

  def add_observer(self,obs):
    """ add a new observer to the model"""
    self.observers.append(obs)

  def notify_observers(self,obj,arg=None):
    """ notify the observers that the model changed"""
    for i in self.observers:
      i.update(obj,arg)



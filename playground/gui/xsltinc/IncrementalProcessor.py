from Ft.Xml.Xslt.Processor import Processor
from ContextTree import ContextTree, ContextTreeNode

class IncrementalProcessor(Processor):
    
    def __init__(self, stylesheetAltUris=None,
                 documentReader=None, implementation=None,
                 stylesheetIncPaths=None):
                 
      # Calling superclass constructor
      Processor.__init__(self, stylesheetAltUris=stylesheetAltUris, 
                         documentReader=documentReader, implementation=implementation,
                         stylesheetIncPaths=stylesheetIncPaths)
      self.contextTree = ContextTree() 

    def applyTemplates(self, context, params=None):
      Processor.applyTemplates(self, context, params=params)
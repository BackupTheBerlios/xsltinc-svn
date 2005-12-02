from logilab.aspects.core import AbstractAspect

class InstantiateMemoizing(AbstractAspect):
    """
    """

    def __init__(self, pointcut):
        """
        """
        AbstractAspect.__init__(self, pointcut)

    def before(self, wobj, context, *args, **kwargs):
        """Before method : we have to store the context.
        """       
        print wobj.__class__.__name__
        print 'CONTEXT: ' + str(args[0])
        print 'PROCESSOR: ' + str(args[1])
        print '='*30
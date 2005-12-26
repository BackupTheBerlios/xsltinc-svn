from Ft import *
import Ft.Xml as Xml
import Dom
from Ft.Xml.Domlette import NonvalidatingReader
from Ft.Xml.Xslt.Processor import Processor as LinearProcessor
from IncrementalProcessor import IncrementalProcessor

from Ft.Xml.InputSource import DefaultFactory


def fromDomToCustomDom(source):
    return Dom.CustomDomDocument(source)


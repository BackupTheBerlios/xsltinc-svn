#!/usr/bin/python
#

from xml.xslt.Processor import Processor

xsltproc = Processor()

xsltproc.appendStylesheetUri("file:///home/t0rt00se/Travail/SILR3/pTrans/testset/persons_to_xhtml_list.xsl")
html = xsltproc.run(DefaultFactory.fromUri("persons.xml"))

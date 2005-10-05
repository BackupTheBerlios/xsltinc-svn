XSLT_ENGINE=xsltproc
FO_ENGINE=fop -q
XSL_FO_SHEET=xsl/weekly_report_fo.xsl 

all: clean
	for src in week*.xml; do \
	 echo $$src | sed "s/xml/pdf/g" | xargs make; \
	done;

%.fo: %.xml
	$(XSLT_ENGINE) --xinclude --output $@ $(XSL_FO_SHEET) $<

%.pdf: %.fo
	$(FO_ENGINE) -fo $< -pdf $@

clean:  
	rm -f *.pdf
	find ./ -name "*~" | xargs rm -f

.PHONY: all clean

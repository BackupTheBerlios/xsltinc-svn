XSLT_ENGINE=xsltproc
FO_ENGINE=fop -q
XSL_FO_SHEET=xsl/weekly_report_fo.xsl 

all: clean
	@for src in week*.xml; do \
	 echo $$src | sed "s/xml/pdf/g" | xargs make; \
	done;

%.fo: %.xml
	$(XSLT_ENGINE) --xinclude --output $@ $(XSL_FO_SHEET) $<

%.pdf: %.fo
	$(FO_ENGINE) -fo $< -pdf $@

biblio: week39.pdf  week40.pdf  week41.pdf  week42.pdf  week43.pdf
	./pdfmerge -o weekly_reports_biblio.pdf week39.pdf  week40.pdf  week41.pdf  week42.pdf  week43.pdf ; echo "finished"

clean:  
	@rm -f *.fo *.pdf
	@find ./ -name "*~" | xargs rm -f

.PHONY: all clean

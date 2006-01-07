DIRNAME_CSS=xhtml-css
DIRNAME_DOCBOOK_XSL=docbook-xsl
DIRNAME_CUSTOM_XSL=custom-xsl
DIRNAME_OUTPUT=output

XSL_TITLEPAGE_TPL=$(DIRNAME_DOCBOOK_XSL)/template/titlepage.xsl

BASENAME_TITLEPAGE_TEMPLATE=$(DIRNAME_CUSTOM_XSL)/titlepage
XSL_XHTML-MONO=$(DIRNAME_CUSTOM_XSL)/xhtml.xsl
XSL_XHTML-CHUNK=$(DIRNAME_CUSTOM_XSL)/xhtml-chunk.xsl
XSL_XHTML-COMMON=$(DIRNAME_CUSTOM_XSL)/xhtml-common.xsl
XSL_COMMON=$(DIRNAME_CUSTOM_XSL)/common.xsl
XSL_FO=$(DIRNAME_CUSTOM_XSL)/fo.xsl

XSLT_ENGINE=xsltproc --xinclude --nonet
FO_ENGINE=fop -q 

all: clean
	@for src in *.xml; do \
	  echo $$src | sed "s/xml/pdf/g" | xargs make; \
	  echo $$src | sed "s/xml/html/g" | xargs make; \
	  echo $$src | sed "s/xml/chunk/g" | xargs make; \
	done;

%.html: %.xml $(XSL_COMMON) $(XSL_XHTML-COMMON) $(XSL_XHTML-MONO)
	$(XSLT_ENGINE) --output $(DIRNAME_OUTPUT)/xhtml-mono/$@ $(XSL_XHTML-MONO) $<
	cp -Rf $(DIRNAME_CSS) $(DIRNAME_OUTPUT)/xhtml-mono

%.chunk: %.xml $(XSL_COMMON) $(XSL_XHTML-COMMON) $(XSL_XHTML-CHUNK)
	$(XSLT_ENGINE) $(XSL_XHTML-CHUNK) $<
	cp -Rf $(DIRNAME_CSS) $(DIRNAME_OUTPUT)/xhtml-chunk
	@echo "" > $(DIRNAME_OUTPUT)/xhtml-chunk/$@

$(BASENAME_TITLEPAGE_TEMPLATE).xsl: $(BASENAME_TITLEPAGE_TEMPLATE).xml
		$(XSLT_ENGINE) --output $(BASENAME_TITLEPAGE_TEMPLATE).xsl \
		$(XSL_TITLEPAGE_TPL) \
		$(BASENAME_TITLEPAGE_TEMPLATE).xml

%.fo: %.xml $(XSL_COMMON) $(XSL_FO) $(BASENAME_TITLEPAGE_TEMPLATE).xsl
	$(XSLT_ENGINE) --output $@ $(XSL_FO) $<

%.pdf: %.fo
	$(FO_ENGINE) -fo $< -pdf $(DIRNAME_OUTPUT)/$@

clean:
	@rm -f $(BASENAME_TITLEPAGE_TEMPLATE).xsl
	@rm -rf $(DIRNAME_OUTPUT)/*
	@find ./ -name "*~" | xargs rm -f 

.PHONY: all clean

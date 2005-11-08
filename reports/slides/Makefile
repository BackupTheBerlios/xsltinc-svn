all: clean 
	@for src in *.tex; do \
	  echo $$src | sed "s/tex/pdf/g" | xargs make; \
	done;

%.pdf: %.tex
	pdflatex $<
	pdflatex $<

clean:
	@for src in *.tex; do \
		ls `echo $$src | sed "s/tex/\*/g"` | grep -v $$src | xargs rm -f ;\
	done;

.PHONY: all clean

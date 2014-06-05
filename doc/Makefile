main.docx: theory.md
	pandoc -o $@ $<
main.pdf: main.dvi
	dvipdfmx $<
main.dvi: main.tex theory.tex
	platex $< 
theory.tex: theory.md
	pandoc -o $@ $<

main.docx: theory.md
	pandoc -o $@ $<
main.pdf: main.dvi
	dvipdfmx $<
main.dvi: main.tex theory.tex
	platex $< 
theory.tex: theory.md
	pandoc -o $@ $<
formula.md: formula.lyx
	grep "begin_inset Formula.*" $< | sed "s/.begin_inset Formula//g" > $@


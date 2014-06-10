main.docx: theory.md
	pandoc -o $@ $<
main.odt: theory.md
	pandoc -o $@ $<
main.pdf: main.dvi
	dvipdfmx $<
main.dvi: main.tex theory.tex
	platex $< 
theory.tex: theory.md
	pandoc -tlatex $< | sed "s/\\\label{.*}//g" > $@
formula.md: formula.lyx
	grep "begin_inset Formula.*" $< | sed "s/.begin_inset Formula//g" > $@
theory.lyx: theory.tex
	tex2lyx -e UTF8 -f $< $@
update:
	-rm theory.md
	nkf -w --overwrite theory.tex
	pandoc -o theory.md theory.tex

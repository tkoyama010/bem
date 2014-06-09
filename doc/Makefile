main.docx: theory.md
	pandoc -o $@ $<
main.pdf: main.dvi
	dvipdfmx $<
main.dvi: main.tex theory.tex
	platex $< 
theory.tex: theory.md
	pandoc -tlatex $< | sed "s/\\\label{.*}//g" > $@
formula.md: formula.lyx
	grep "begin_inset Formula.*" $< | sed "s/.begin_inset Formula//g" > $@
theory.pdf: theory.dvi
	dvipdfmx $<
theory.dvi: theory.tex
	platex $< 
theory.lyx: theory.tex
	tex2lyx -e UTF8 -f $< $@
theory.md:
	pandoc -o $@ theory.tex
clean:
	rm theory.md

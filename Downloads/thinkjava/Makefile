LATEX = latex

DVIPS = dvips

PDFFLAGS = -dCompatibilityLevel=1.4 \
           -dCompressPages=true -dUseFlateCompression=true  \
           -dEmbedAllFonts=true -dSubsetFonts=true -dMaxSubsetPct=100

FIGS = $(addprefix figs/, \
    java assign stack stack2 stack3 assign2 reference rectangle rectangle2 \
    aliasing aliasing2 reference2 reference3 time array array2 array3      \
    stringarray card cardarray cardarray2 deckobject subdeck LifeRunner    \
    circle coordinates mickey moose moire)

PDFFIGS = $(addsuffix .pdf,$(FIGS))

default: thinkjava.pdf

thinkjava.pdf: $(PDFFIGS) version.tex latexonly

version.tex: .git/index
	echo '\def\gitversion{'`git describe --tags --always --dirty=+`'}' >$@

%.pdf: %.tex
	xelatex -halt-on-error  $* && makeindex $* && xelatex $*

%.pdf: %.eps
	epstopdf $<

all:	thinkjava.tex
	latex thinkjava
	makeindex thinkjava
	latex thinkjava
	dvips -Ppdf -o thinkjava.ps thinkjava
	ghostview thinkjava.ps

pdf:	thinkjava.ps
	ps2pdf $(PDFFLAGS) thinkjava.ps thinkjava.pdf

clean:
	rm -f *~ *.aux *.log *.dvi *.idx *.ilg *.ind *.toc

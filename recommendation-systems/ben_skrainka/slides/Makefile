# Build lecture slides for time series

# Commands
PANDOC = pandoc -t beamer --template=../config/default.beamer
RM = rm -f

# Files
TGT = bss-lecture.pdf

# Rules
default: $(TGT)

lecture: default

all: default

clean:
	$(RM) $(TGT) notes.pdf

%.pdf : %.md
	$(PANDOC) $< -o $@

notes: notes.md
	pandoc notes.md -t latex -o notes.pdf

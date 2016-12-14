# Commands
# PANDOC = pandoc -t beamer --template=../config/default.beamer
PANDOC = pandoc -t beamer -V theme:metropolis #--template=./default.beamer
RM = rm -f

# Files
TGT = intro_to_python.pdf

# Rules
default: $(TGT)

lecture: default

all: default

clean:
	$(RM) $(TGT)

%.pdf : %.md
	$(PANDOC) $< -o $@

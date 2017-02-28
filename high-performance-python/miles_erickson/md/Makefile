# Build lecture slides

# Commands
PANDOC = pandoc -t beamer --template=config/g.beamer
RM = rm -f

# Files
HPP = me-hpp.pdf
AWS = me-aws.pdf

# Rules
default: $(HPP) $(AWS)

lecture: default

all: default

%.pdf : %.md
	$(PANDOC) $< -o $@

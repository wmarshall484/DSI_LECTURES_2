# Build lecture slides for sql lecture

# Commands
PANDOC = pandoc -t beamer --template=./config/default.beamer
RM = rm -f

# Files
TGT = me-sql-lecture.pdf

# Rules
default: $(TGT)

lecture: default

all: default

clean:
	$(RM) $(TGT)

%.pdf : %.md
	$(PANDOC) $< -o $@

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
	$(RM) $(TGT)

%.pdf : %.md
	$(PANDOC) $< -o $@

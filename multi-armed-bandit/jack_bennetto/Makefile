# Build lecture slides for time series

# Commands
PANDOC = pandoc -t beamer --template=./default.beamer
RM = rm -f

# Files
TGT = jb-multi-armed-bandit.pdf

# Rules
default: $(TGT)

lecture: default

all: default

clean:
	$(RM) $(TGT)

%.pdf : %.md
	$(PANDOC) $< -o $@

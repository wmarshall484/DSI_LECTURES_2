# Build lecture slides for time series

# Commands
# PANDOC = pandoc -t beamer --template=../config/default.beamer
PANDOC = pandoc -t beamer -V theme:metropolis
RM = rm -f

# Files
TGT = multi-arm-bandit-slides.pdf

# Rules
default: $(TGT)

lecture: default

all: default

clean:
	$(RM) $(TGT)

%.pdf : %.md
	$(PANDOC) $< -o $@

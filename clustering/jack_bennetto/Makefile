# Build lecture slides for time series

# Commands
PANDOC = pandoc -t beamer --filter=./overlay_filter --template=./default.beamer
RM = rm -f

# Files
TGT = jb-clustering.pdf

# Rules
default: $(TGT)

lecture: default

all: default

clean:
	$(RM) $(TGT)

%.pdf : %.md
	$(PANDOC) $< -o $@

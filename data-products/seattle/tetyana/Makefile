# Build lecture slides for

# Commands
PANDOC = pandoc -t beamer --template=./default.beamer
RM = rm -f

# Files
TGT = lecture.pdf

# Rules
default: $(TGT)

lecture: default

all: default

clean:
	$(RM) $(TGT)

%.pdf : %.md
	$(PANDOC) $< -o $@

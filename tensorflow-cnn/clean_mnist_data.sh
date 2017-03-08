#! /bin/bash

# Collapse multiple consecutive spaces into a single space and then
# remove all spaces at the beginning of a line.
cat $1 | sed "s/  */ /g" | sed "s/^ *//g" > $1.temp
# Overwrite original files with temporary files.
mv $1.temp $1

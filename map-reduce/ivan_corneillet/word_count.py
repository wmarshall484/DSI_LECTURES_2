#!/usr/bin/env python

from mrjob.job import MRJob
from string import punctuation

class MRWordCount(MRJob):

  def mapper(self, _, line):
    for word in line.split():
      word = word.strip(punctuation).lower()
      yield (word, 1)

  def reducer(self, word, counts):
    yield (word, sum(counts))

if __name__ == '__main__':
  MRWordCount.run()

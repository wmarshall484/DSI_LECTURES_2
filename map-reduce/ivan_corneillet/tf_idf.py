#!/usr/bin/env python

from mrjob.job import MRJob
from mrjob.step import MRStep
from itertools import tee
import numpy as np

class MRTfIdf(MRJob):

  def steps(self):
    return [
      MRStep(mapper = self.round_1_mapper,
        reducer = self.round_1_reducer),

      MRStep(mapper = self.round_2_mapper,
        reducer = self.round_2_reducer),

      MRStep(mapper = self.round_3_mapper,
        reducer = self.round_3_reducer)
    ]

  # FIRST ROUND: Word counts for each word in each document
  #   Input: document
  #   Output: ((word, doc_id), word_count)

  def round_1_mapper(self, _, doc):
    doc = doc.split()

    total_docs = doc[0]
    doc_id = doc[1]
    words = doc[2:]

    for word in words:
      yield ((word, doc_id, total_docs), 1)

  def round_1_reducer(self, (word, doc_id, total_docs), word_count):
    yield ((word, doc_id, total_docs), sum(word_count))

  # SECOND ROUND: Number of words for each document
  #   Input: ((word, doc_id), word_count)
  #   Output: ((word, doc_id), (word_count, words_per_doc)

  def round_2_mapper(self,
                     (word, doc_id, total_docs),
                     word_count):

    yield ((doc_id, total_docs), (word, word_count))

  def round_2_reducer(self,
                      (doc_id, total_docs),
                      words_and_word_counts):

    l1, l2 = tee(words_and_word_counts)

    words_per_doc = sum(map(lambda (_, word_count): word_count, l1))

    for (word, word_count) in l2:
      yield ((word, doc_id, total_docs), (word_count, words_per_doc))

  # THIRD ROUND: TF-IDF
  #   Input: ((word, doc_id), (word_count, words_per_doc)
  #   Output: ((word, doc_id), tf_idf)

  def round_3_mapper(self,
                     (word, doc_id, total_docs),
                     (word_count, words_per_doc)):

    yield ((word, total_docs), (doc_id, word_count, words_per_doc))

  def round_3_reducer(self,
                      (word, total_docs),
                      doc_ids_word_counts_and_words_per_docs):

    total_docs = float(total_docs)

    l1, l2 = tee(doc_ids_word_counts_and_words_per_docs)

    docs_per_word = len(list(l1))

    for (doc_id, word_count, words_per_doc) in l2:
      tf = 1. * word_count / words_per_doc
      idf = np.log(total_docs / docs_per_word)
      tf_idf = tf * idf

      yield ((word, doc_id), tf_idf)

if __name__ == '__main__':
  MRTfIdf.run()

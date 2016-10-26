from mrjob.job import MRJob
from string import punctuation

class WordCount(MRJob):
    """Hello World!"""

    def mapper(self, _, line):
        for word in line.split():
            for char in punctuation:
                word = word.replace(char, "")
            yield (word.replace(punctuation, ""), 1)

    def combiner(self, word, counts):
        yield(word, sum(counts))

    def reducer(self, word, counts):
        yield (word, sum(counts))


if __name__ == '__main__':
    WordCount.run()

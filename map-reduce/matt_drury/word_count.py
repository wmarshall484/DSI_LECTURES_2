from mrjob.job import MRJob

class WordCount(MRJob):

    def mapper(self, _, line):
        for word in line.split():
            yield (word, 1)

    def reducer(self, word, counts):
        yield ('{:09d}'.format(sum(counts)), word)


if __name__ == '__main__':
    WordCount.run()

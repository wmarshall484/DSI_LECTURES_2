from mrjob.job import MRJob

class WordCount(MRJob):

    def mapper(self, _, line):
        pass

    def reducer(self, word, counts):
        pass


if __name__ == '__main__':
    WordCount.run()

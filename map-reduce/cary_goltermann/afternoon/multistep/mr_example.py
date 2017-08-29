from mrjob.job import MRJob
from mrjob.step import MRStep
from string import punctuation

class MRAverage(MRJob):
    def mapper1(self, _, line):
        clean_line = ''.join(c for c in line if c not in punctuation)
        for word in clean_line.lower().split():
            yield word, 1

    def reducer1(self, word, counts):
        yield word, sum(counts)

    def mapper2(self, word, count):
        yield word[0], (word, count)

    def reducer2(self, letter, word_lengths):
        yield letter, max(word_lengths, key=lambda x: x[1])

    def steps(self):
        return [MRStep(mapper=self.mapper1, reducer=self.reducer1),
                MRStep(mapper=self.mapper2, reducer=self.reducer2)]

if __name__ == '__main__':
    MRAverage.run()

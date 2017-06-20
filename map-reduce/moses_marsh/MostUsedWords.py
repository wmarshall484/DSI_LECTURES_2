from mrjob.job  import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class MostUsedWords(MRJob):

    def mapper_get_words(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def reducer_count_words(self, word, counts):
        count_sum = '{:0>5}'.format(sum(counts))
        yield (count_sum, word)

    def reducer_sort(self, count, words):
        for word in words:
            yield (word, count)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_sort)
        ]

if __name__ == '__main__':
    MostUsedWords.run()
"""
How to do a intersection (from relational algebra) using MapReduce.
"""

from mrjob.job import MRJob

class IntersectionJob(MRJob):

    def mapper(self, _, line):
        yield (line, 0)

    def reducer(self, key, values):
        if len(list(values)) >= 2:
            yield (key, None)

if __name__ == '__main__':
     IntersectionJob.run()

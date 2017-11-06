"""
How to do a union (from relational algebra) using MapReduce.
"""

from mrjob.job import MRJob

class UnionJob(MRJob):

    def mapper(self, _, line):
        yield (line, 0)

    def reducer(self, key, values):
        yield (key, None)

if __name__ == '__main__':
     UnionJob.run()

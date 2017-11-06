"""
How to do a group-by / aggregation (from relational algebra) using MapReduce.
"""

import numpy as np
from mrjob.job import MRJob

class GroupByJob(MRJob):

    def mapper(self, _, line):
        date, outlook, temperature, humidity, windy = line.split(',')
        yield (outlook, float(temperature))

    def reducer(self, key, values):
        yield (key, np.mean(list(values)))

if __name__ == '__main__':
     GroupByJob.run()

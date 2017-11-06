"""
How to do a selection (from relational algebra) using MapReduce.
"""

from mrjob.job import MRJob

class SelectionJob(MRJob):

    def mapper(self, _, line):
        date, outlook, temperature, humidity, windy = line.split(',')
        if outlook == 'sunny':
            yield ((date, outlook, temperature, humidity, windy), 0)

    def reducer(self, key, values):
        yield key, None

if __name__ == '__main__':
     SelectionJob.run()

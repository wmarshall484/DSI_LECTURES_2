"""
How to do a difference (from relational algebra) using MapReduce.
"""

import os
from mrjob.job import MRJob

class DifferenceJob(MRJob):

    def mapper(self, _, line):
        file_path = os.environ['map_input_file']
        yield (line, '1' in file_path)

    def reducer(self, key, values):
        values = list(values)
        if values == [True]:
            yield (key, None)

if __name__ == '__main__':
     DifferenceJob.run()

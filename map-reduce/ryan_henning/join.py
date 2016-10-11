"""
How to do a join (from relational algebra) using MapReduce.
"""

import os
from itertools import product
from mrjob.job import MRJob

class JoinJob(MRJob):

    def mapper(self, _, line):
        file_path    = os.environ['map_input_file']
        parts        = line.split(',')
        join_on      = parts[0]
        other_values = parts[1:]
        yield (join_on, (file_path, other_values))

    def reducer(self, key, values):
        values = list(values)
        file_paths = list(set([v[0] for v in values]))
        if len(file_paths) != 2:
            raise Exception('A join must operate on exactly two relations.')
        left_values  = [v[1] for v in values if v[0] == file_paths[0]]
        right_values = [v[1] for v in values if v[0] == file_paths[1]]
        for l, r in product(left_values, right_values):
            yield (key, l + r)

if __name__ == '__main__':
     JoinJob.run()

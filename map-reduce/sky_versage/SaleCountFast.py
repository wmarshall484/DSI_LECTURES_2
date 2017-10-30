from mrjob.job import MRJob
import numpy as np

class SaleCountFast(MRJob):
    def mapper(self, _, line):
        if line.startswith('#'):
            return
        fields = line.split()
        state = fields[3]
        yield (state, 1)
    def combiner(self, state, counts): 
        yield state, sum(counts)
    def reducer(self, state, counts): 
        yield state, sum(counts)
if __name__ == '__main__': 
    SaleCountFast.run()
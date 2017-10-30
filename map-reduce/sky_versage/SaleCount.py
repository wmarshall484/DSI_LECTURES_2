from mrjob.job import MRJob

class SaleCount(MRJob):
    def mapper(self, _, line):
        if line.startswith('#'):
            return
        fields = line.split()
        state = fields[3]
        revenue = float(fields[-1])
        yield (state, 1)
    def reducer(self, state, trans): 
        yield (state, sum(trans))
if __name__ == '__main__': 
    SaleCount.run()
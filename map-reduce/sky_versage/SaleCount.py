from mrjob.job import MRJob

class SaleCount(MRJob):
    def mapper(self, _, line):
        if line.startswith('#'):
            return
        fields = line.split()
        store = fields[2]
        state = fields[3]
        revenue = float(fields[-1])
        yield (state, 1)
    def reducer(self, store, revenue): 
        yield (store, sum(revenue))
if __name__ == '__main__': 
    SaleCount.run()
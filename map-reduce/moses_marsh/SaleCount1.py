from mrjob.job  import MRJob
class SaleCount1(MRJob):
    def mapper(self, _, line):
        if line.startswith('#'): return
        fields = line.split()
        state = fields[3]
        if state == 'CA':
            self.increment_counter('State', 'CA', 1)
        if state == 'WA':
            self.increment_counter('State', 'WA', 1)
if __name__ == '__main__': 
    SaleCount1.run()
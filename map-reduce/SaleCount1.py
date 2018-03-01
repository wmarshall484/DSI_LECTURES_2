from mrjob.job  import MRJob
from mrjob.step import MRStep
class SaleCount1(MRJob):
    def mapper_count(self, _, line):
        if line.startswith('#'): return
        fields = line.split()
        state = fields[3]
        if state == 'CA':
            self.increment_counter('State', 'CA', 1)
        if state == 'WA':
            self.increment_counter('State', 'WA', 1)
    def steps(self):
        return [
            MRStep(mapper=self.mapper_count)
        ]
if __name__ == '__main__': 
    SaleCount1.run()
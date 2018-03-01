from mrjob.job  import MRJob
from mrjob.step import MRStep
class SaleExtract(MRJob):
    def mapper_extract(self, _, line):
        if line.startswith('#'): return
        fields = line.split()
        state = fields[3]
        if state != 'CA': return
        yield (state, line)
    def steps(self):
        return [
            MRStep(mapper=self.mapper_extract)
        ]
if __name__ == '__main__': 
    SaleExtract.run()
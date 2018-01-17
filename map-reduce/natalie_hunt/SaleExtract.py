from mrjob.job  import MRJob
class SaleExtract(MRJob):
    def mapper(self, _, line):
        if line.startswith('#'): 
            return
        fields = line.split()
        state = fields[3]
        if state != 'CA': 
            return
        yield (state, line)

if __name__ == '__main__': 
    SaleExtract.run()
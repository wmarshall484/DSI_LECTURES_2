from mrjob.job import MRJob
class Join(MRJob):
    def mapper(self, _, line):
        if line.startswith('#'):
            return
        fields = line.split('|')
        if len(fields) == 2:
            yield (fields[1], fields[0])
        else:
            yield (fields[2], ', '.join([fields[1], fields[0]]))

#     def reducer(self, key, info):
#         try:
#             info = ' '.join(info)
#         except:
#             pass
#         yield (key, info)
        
if __name__ == '__main__': 
    Join.run()
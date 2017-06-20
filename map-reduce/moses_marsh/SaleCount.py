from mrjob.job  import MRJob
from mrjob.step import MRStep
import numpy as np
class SaleCount(MRJob):
  
   def mapper1(self, _, line):
       if line.startswith('#'):
           return
       fields = line.split()
       amount = float(fields[5])
       state = fields[3]
       yield (state, amount)

   def reducer1(self, state, amounts):
       amount = '{amt:09.2f}'.format(amt=sum(amounts)) 
       yield (state, amount)
   
   def mapper2(self, state, amount):
       yield (amount, state)

   def reducer2(self, amount, states):
       for state in states: 
           yield (state, amount)
   
   def steps(self):
       return [
           MRStep(mapper=self.mapper1, reducer=self.reducer1),
           MRStep(mapper=self.mapper2, reducer=self.reducer2)
       ]
if __name__ == '__main__': 
   SaleCount.run()
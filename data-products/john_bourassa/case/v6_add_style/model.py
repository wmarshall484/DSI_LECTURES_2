import pandas as pd

class DataModel(object):
    def __init__(self):
        self.data = pd.read_csv("data/equations.csv")
	
    def get_prior_equations(self):
        return self.data.tail(5).to_dict("records")
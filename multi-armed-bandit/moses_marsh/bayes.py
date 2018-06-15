import matplotlib.pyplot as plt


class Bayes(object):
    def __init__(self, prior, likelihood_func):
        '''
        INPUT:
        prior (dict): key is the value (e.g. 4-sided die),
                      value is the probability

        likelihood_func (function): takes a new piece of data and the value and
                                    outputs the likelihood of getting that data
        '''
        self.prior = prior
        self.likelihood_func = likelihood_func
    def normalize(self):
        '''
        INPUT: None
        OUTPUT: None

        Makes the sum of the probabilities equal 1.
        '''
        total = float(sum(self.prior.values()))
        for key in self.prior:
            self.prior[key] /= total

    def update(self, data):
        '''
        INPUT:
            data (int or str): A single observation (data point)

        OUTPUT: None
        
        Conduct a bayesian update. Multiply the prior by the likelihood and
        make this the new prior.
        '''
        for key in self.prior:
            self.prior[key] *= self.likelihood_func(data, key)
        self.normalize()

    def print_distribution(self):
        '''
        Print the current posterior probability.
        '''
        sorted_keys = sorted(self.prior.keys())
        for key in sorted_keys:
            print("{}: {}".format(key, self.prior[key]))

    def plot(self, title=None, **kwargs):
        '''
        Plot the current prior.
        '''
        sorted_keys = sorted(self.prior.keys())
        sorted_probs = [self.prior[key] for key in sorted_keys]
        plt.plot(sorted_keys, sorted_probs, **kwargs)
        plt.title(title)

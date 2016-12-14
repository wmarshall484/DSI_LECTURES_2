import numpy as np
from scipy import stats 
import matplotlib.pyplot as plt
import matplotlib

class t_hypothesis_test(object):
    '''
    attributes:
    mu_0: null hypothesis H_0
    sample_standard_deviation: observed (or proposed) standard deviation
    mu: true mean
    effect_size:  mu - mu_0
    n: sample size
    alpha: significance level
    tails: "both", "upper" or "lower" for two-tailed versus one-tailed tests
    self.se: standard error
    test_statistics

    methods:
    set_null_hypothesis
    set_test
    set_truth
    set_sampleSize                             

    plot_null
    plot_power
    evaluate_testStatistic    
    '''
    
    def __init__(self):
        self.mu_0 = 0
        self.sample_standard_deviation = 1
        self.alpha = 0.05
        self.tails = "both"
        self.mu = 3
        self.effect_size = self.mu - self.mu_0
        self.n = 10
        self.se = self.sample_standard_deviation/self.n**.5


    def set_null_hypothesis(self, mu_0 = 0, sample_standard_deviation = 1):
        self.mu_0 = mu_0
        self.sample_standard_deviation = sample_standard_deviation
        self.se = self.sample_standard_deviation/self.n**.5

    def set_test(self, alpha = 0.05, tails = "both"):
        self.alpha = alpha
        self.tails = tails

    def set_truth(self, mu = 0, sample_standard_deviation = 1):
        self.mu = mu
        self.effect_size = self.mu-self.mu_0
        self.sample_standard_deviation = sample_standard_deviation
        self.se = self.sample_standard_deviation/self.n**.5

    def set_sampleSize(self, n=30):
        self.n = n
        self.se = self.sample_standard_deviation/self.n**.5

    def plot_null(self):
        if self.tails == "both":
            tail_area = self.alpha/2
            tail_color = ['red','green','red']
        elif self.tails == "upper":
            tail_area = self.alpha
            tail_color = ['green','green','red']
        else: 
            tail_area = self.alpha
            tail_color = ['red','green','green']

        t_critical = stats.t.ppf(1-tail_area, self.n-1)
        x_lower = np.linspace(self.mu_0-3*t_critical*self.se, self.mu_0-t_critical*self.se, 100)
        x_middle = np.linspace(self.mu_0-t_critical*self.se, self.mu_0+t_critical*self.se, 100)
        x_upper = np.linspace(self.mu_0+t_critical*self.se, self.mu_0+3*t_critical*self.se, 100)
        x = np.concatenate((x_lower,x_middle,x_upper))
        mxht = max(stats.t.pdf(x, self.n-1, self.mu_0, self.se))
        sm4pc = (min([self.mu_0,self.mu]) - min([self.mu_0,self.mu]) + 3*t_critical*self.se)/mxht
        plt.plot(x, sm4pc*stats.t.pdf(x, self.n-1, self.mu_0, self.se), color='k', linewidth=3)
        plt.fill_between(x_lower, sm4pc*stats.t.pdf(x_lower, self.n-1, self.mu_0, self.se), 0, alpha=.3, color=tail_color[0])
        plt.fill_between(x_middle, sm4pc*stats.t.pdf(x_middle, self.n-1, self.mu_0, self.se), 0, alpha=.3, color=tail_color[1])
        plt.fill_between(x_upper, sm4pc*stats.t.pdf(x_upper, self.n-1, self.mu_0, self.se), 0, alpha=.3, color=tail_color[2])
        plt.xlim([min([self.mu_0,self.mu]) - 1.5*t_critical*self.se, max([self.mu_0,self.mu]) + 1.5*t_critical*self.se])
        plt.text(self.mu_0, .5*sm4pc*mxht, "significance level = " + str(round(self.alpha,3)), fontsize=8, ha="center")
        plt.text(self.mu_0, .4*sm4pc*mxht, "alpha = Pr(Type I error) = " + str(round(self.alpha,3)), fontsize=8, ha="center")
        plt.text(self.mu_0, .3*sm4pc*mxht, "(Specificity = " + str(round(1 - self.alpha,3)) + ")", fontsize=8, ha="center")

    def plot_power(self):
        if self.tails == "both":
            tail_area = self.alpha/2
        else: 
            tail_area = self.alpha
        t_critical = stats.t.ppf(1-tail_area, self.n-1)
        x = np.linspace(self.mu-3*t_critical*self.se, self.mu+3*t_critical*self.se, 300)
        mxht = max(stats.t.pdf(x, self.n-1, self.mu_0, self.se))
        sm4pc = (min([self.mu_0,self.mu]) - min([self.mu_0,self.mu]) + 3*t_critical*self.se)/mxht
        plt.plot(x, sm4pc*stats.t.pdf(x, self.n-1, self.mu, self.se), color='k', linewidth=3)
        if self.tails == "upper" or (self.tails == "both" and self.mu > self.mu_0):
            x_reject = np.linspace(self.mu_0+t_critical*self.se, self.mu+3*t_critical*self.se, 100)
            x_accept = np.linspace(self.mu-3*t_critical*self.se, self.mu_0+t_critical*self.se, 100)
            power = round(1 - stats.t.cdf(self.mu_0 + t_critical*self.se, df = self.n - 1, loc = self.mu, scale = self.se),2)
        if self.tails == "lower" or (self.tails == "both" and self.mu_0 > self.mu):
            x_reject = np.linspace(self.mu-3*t_critical*self.se, self.mu_0-t_critical*self.se, 100)
            x_accept = np.linspace(self.mu_0-t_critical*self.se, self.mu-3*t_critical*self.se, 100)
            power = round(stats.t.cdf(self.mu_0 - t_critical*self.se, df = self.n -1, loc = self.mu, scale = self.se),2)
        plt.fill_between(x_reject, sm4pc*stats.t.pdf(x_reject, self.n-1, self.mu, self.se), 0, alpha=.3, color="blue")
        plt.fill_between(x_accept, sm4pc*stats.t.pdf(x_accept, self.n-1, self.mu, self.se), 0, alpha=.3, color="yellow")
        plt.xlim([min([self.mu_0,self.mu]) - 1.5*t_critical*self.se, max([self.mu_0,self.mu]) + 1.5*t_critical*self.se])
        plt.text(self.mu, .5*sm4pc*mxht, "power = " + str(power), fontsize=8, ha="center")
        plt.text(self.mu, .4*sm4pc*mxht, "1 - Pr(Type II error) = " + str(power), fontsize=8,ha="center")
        plt.text(self.mu, .3*sm4pc*mxht, "(Sensitivity = " + str(power) + ")", fontsize=8,ha="center")

    def evaluate_testStatistic(self, xBar, show_likelihood_ratio = False):
        if self.tails == "both":
            p_value = 2 * (1 - stats.t.cdf(abs(xBar-self.mu_0)/self.se, df = self.n - 1))
            tail_color = ["k","k"]
            tail_alpha = [.8,.8]
            tail_area = self.alpha/2
            pos = 1
        elif self.tails == "upper" and xBar > self.mu_0:
            p_value = 1 - stats.t.cdf(xBar, loc = self.mu_0, scale = self.se, df = self.n - 1)
            tail_color = [None, "k"]
            tail_alpha = [0,.8]
            tail_area = self.alpha
            pos = 1
        elif self.tails == "lower" and xBar < self.mu_0:
            p_value = stats.t.cdf(xBar, loc = self.mu_0, scale = self.se, df = self.n - 1)
            tail_color = ["k", None]
            tail_alpha = [.8, 0]
            tail_area = self.alpha
            pos = -1
        else: 
            print "not implemented"
        t_value = (abs(xBar)-self.mu_0)/self.se
        t_critical = stats.t.ppf(1-tail_area, self.n-1)
        x = np.linspace(self.mu_0-3*t_critical*self.se, self.mu_0+3*t_critical*self.se, 300)
        mxht = max(stats.t.pdf(x, self.n-1, self.mu_0, self.se))
        sm4pc = (min([self.mu_0,self.mu]) - min([self.mu_0,self.mu]) + 3*t_critical*self.se)/mxht

        plt.plot(x, sm4pc*stats.t.pdf(x, self.n-1, self.mu_0, self.se), color='k', linewidth=3)
        x_lower = np.linspace(self.mu_0-3*t_critical*self.se, self.mu_0-t_value*self.se, 300)
        x_upper = np.linspace(self.mu_0+t_value*self.se, self.mu_0+3*t_critical*self.se, 300) 
        plt.fill_between(x_lower, sm4pc*stats.t.pdf(x_lower, self.n-1, self.mu_0, self.se), 0, alpha=tail_alpha[0], color=tail_color[0])
        plt.fill_between(x_upper, sm4pc*stats.t.pdf(x_upper, self.n-1, self.mu_0, self.se), 0, alpha=tail_alpha[1], color=tail_color[1])
        plt.text(pos*(t_value-self.mu_0)*self.se, .2*sm4pc*mxht, "   p-value = " + str(round(p_value,3)), fontsize=8)

        if show_likelihood_ratio:
            x = np.linspace(self.mu-3*t_critical*self.se, self.mu+3*t_critical*self.se, 300)
            plt.plot(x, sm4pc*stats.t.pdf(x, self.n-1, self.mu, self.se), color='k', linewidth=3)
            d_mu_xBar = sm4pc*stats.t.pdf(xBar, self.n-1, self.mu, self.se)
            d_mu_xBar_0 = sm4pc*stats.t.pdf(xBar, self.n-1, self.mu_0, self.se)
            plt.plot([xBar + .05 * self.se]*2, [0, d_mu_xBar], color="blue",linewidth=5)
            plt.plot([xBar - .05 * self.se]*2, [0, d_mu_xBar_0], color="red",linewidth=5)
            plt.plot([xBar + .05 * self.se]*2, [0, d_mu_xBar], color="yellow",linewidth=5, linestyle=":")
            plt.plot([xBar - .05 * self.se]*2, [0, d_mu_xBar_0], color="yellow",linewidth=5, linestyle=":")
            matplotlib.rcParams.update({'font.size': 8})
            plt.pie([d_mu_xBar/(d_mu_xBar+d_mu_xBar_0),d_mu_xBar_0/(d_mu_xBar+d_mu_xBar_0)],
                    labels = ["Likelihood of H_a", "Likelihood of H_0"],frame=True, colors=["blue","red"], 
                    autopct="%.0f%%",startangle=-45,
                    center=(self.mu, .6*sm4pc*mxht), radius = .75*self.se)
        plt.xlim([min([self.mu_0,self.mu]) - 1.5*t_critical*self.se, max([self.mu_0,self.mu]) + 1.5*t_critical*self.se])


if __name__ == "__main__":
    my_hyp_test = t_hypothesis_test()
    my_hyp_test.set_null_hypothesis(mu_0=0, sample_standard_deviation=1)
    my_hyp_test.set_test(alpha=.1,tails="both")

    my_hyp_test.set_truth(mu=1, sample_standard_deviation=1)
# other 
    my_hyp_test.set_test(alpha=.05,tails="upper")
    my_hyp_test.set_truth(mu=.02, sample_standard_deviation=(2*.05*.95)**.5)
    my_hyp_test.set_sampleSize(n=1000)

    fig = plt.figure(1)

    plt.subplot(221)
    my_hyp_test.plot_null()


    plt.subplot(222)

    fig = plt.figure(2)
    my_hyp_test.plot_null()
    my_hyp_test.plot_power()
    plt.xlim(-.03,.05)
# other
    plt.xlabel("n + n = 2000")

    fig = plt.figure(1)

    plt.subplot(223)
    my_hyp_test.plot_null()
#    my_hyp_test.evaluate_testStatistic(.65)
    my_hyp_test.evaluate_testStatistic(.012)

    plt.subplot(224)
    my_hyp_test.plot_null()
#    my_hyp_test.evaluate_testStatistic(.65, show_likelihood_ratio=True)
    my_hyp_test.evaluate_testStatistic(.012, show_likelihood_ratio=True)

    plt.tight_layout()
    plt.show()

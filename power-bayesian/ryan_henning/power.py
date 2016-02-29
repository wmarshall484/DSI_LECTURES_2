import scipy.stats as st
from math import sqrt


def calc_min_sample_size(alpha, power, s, mean_desired, mean_original):
    '''
    alpha is in (0, 1), the type-I error we're allowing for our
    experiment. Typically, alpha=0.05.

    power is in (0, 1), it determines the probability of detecting
    the desired mean ("effect size") under the alternative hypothesis.
    It is 1-beta, where beta is the type-II error we're allowing
    for our experiment. Typically, power=0.9.

    s is the estimate of the standard deviation of the two hypothesised
    distributions.

    mean_desired is the mean we're trying to detect -- it is the mean
    of the candidate alternative hypothesis.

    mean_original is the mean of the null hypothesis.
    '''

    Z_alpha = st.norm.ppf(alpha)
    Z_power = st.norm.ppf(power)

    return ((Z_power - Z_alpha) * s / (mean_desired - mean_original)) ** 2


if __name__ == '__main__':

    mean_original = float(raw_input('original mean (mean of H0): '))
    mean_desired  = float(raw_input('desired mean  (mean of HA): '))

    std_dev = float(raw_input('estimate of standard deviation: '))

    alpha = float(raw_input('alpha: '))
    power = float(raw_input('power: '))

    print "min samples needed:", calc_min_sample_size(alpha, power,
                                      std_dev, mean_desired, mean_original)


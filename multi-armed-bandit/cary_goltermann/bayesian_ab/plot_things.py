import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta

def plot_beta(ax, x, a, b):
    y = beta.pdf(x, a, b)
    ax.plot(x, y, lw=3, label=r'$\alpha = {}, \beta = {}$'.format(a, b))


def plot_betas(asbs, save_fig=False):
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111)
    x = np.arange(0, 1.005, 0.005)
    for a, b in asbs:
        plot_beta(ax, x, a, b)
    ax.legend(prop={'size':20})
    fig.suptitle('Beta Distribution', fontsize=30)
    
    if save_fig:
        plt.savefig('images/betas.png')
    else:
        plt.show()


def plot_site_comparison(num_conv_a, num_views_a, num_conv_b, num_views_b,
                         effect_size=0, alpha=1, beta=1, num_samples=10000):
    site_a_simulation = np.random.beta(num_conv_a + alpha,
                                       num_views_a - num_conv_a + beta,
                                       size=num_samples)
    site_b_simulation = np.random.beta(num_conv_b + alpha,
                                       num_views_b - num_conv_b + beta,
                                       size=num_samples)
    fig = plt.figure(figsize=(7, 8))
    ax = fig.add_subplot(111)
    a_label = '$p_A' + (' + {}$'.format(effect_size) if effect_size else '$')
    ax.hist(site_a_simulation + effect_size, bins=100, alpha=0.3, label=a_label)
    ax.hist(site_b_simulation, bins=100, alpha=0.3, label='$p_B$')
    ax.set_xlim([0.45, 0.75])
    ax.legend()
    fig.suptitle("Histogram of posterior $p's$ for site A & B", fontsize=20)
    plt.show()


if __name__ == '__main__':
    np.random.seed(42)
    plot_site_comparison(312, 543, 371, 580, 0.05)

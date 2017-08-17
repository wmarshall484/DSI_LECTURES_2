import numpy as np
import scipy.stats as scs


def plot_power(ax, n, sigma, effect_size, 
               alpha=None, beta=False, power=False, x_labels=False):
    standard_error = sigma / n**0.5
    x = np.linspace(-0.2, 0.5, 200)


    h0 = scs.norm(0, standard_error)
    ha = scs.norm(effect_size, standard_error)
    
    if alpha:
        critical_value = h0.ppf(1 - alpha)
        xpos = x[x >= critical_value]
        xneg = x[x <= critical_value]

    ax.plot(x, h0.pdf(x), color='red', label='$H_0$')
    ax.plot(x, ha.pdf(x), color='blue', label='$H_A$')

    if power:
        ax.fill_between(xpos, 0, ha.pdf(xpos), color='black', hatch='////', alpha=0.2, label="Power")
    if alpha:
        ax.axvline(critical_value, color='black', linestyle='--')
        ax.fill_between(xpos, 0, h0.pdf(xpos), color='red', alpha=0.2, label=r"$\alpha$")
    if beta:
        ax.fill_between(xneg, 0, ha.pdf(xneg), color='blue', alpha=0.2, label="$\\beta$")

    ax.set_ylim(ymin=0.0)
    ax.set_xlim(-0.2, 0.5)
    ax.legend()
    
    if x_labels:
        ax.get_xaxis().set_visible(False)
        ax.axvline(0.0, color='red', linestyle='--')
        ax.text(0.0, -0.5, "$\mu_0$", fontsize=20, color="red",
                horizontalalignment='center', verticalalignment='center')
        ax.axvline(effect_size, color='blue', linestyle='--')
        ax.text(effect_size, -0.5, "$\mu_a$", fontsize=20, color="blue",
                horizontalalignment='center', verticalalignment='center')
        ax.text(critical_value, -0.5, "RT", fontsize=16,
                horizontalalignment='center', verticalalignment='center')

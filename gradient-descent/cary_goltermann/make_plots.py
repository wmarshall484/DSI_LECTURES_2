import numpy as np
import matplotlib.pyplot as plt


def plot_one_var_ex():
    """Plots the one variable graph at beginning of notes.
    """
    fig, ax = plt.subplots(1, figsize=(4, 3))
    xs = np.linspace(-1.2, 8, 100)
    ys = -((1./4)*xs**4 - (10./3)*xs**3 + (27./2)*xs**2 - 18*xs)
    ax.plot(xs, ys, color='k', lw=1.5, label='f(x)')

    ax.axhline(0, color='gray')
    ax.axvline(0, color='gray')
    ax.vlines(6, 0, 18, color='k', linestyles='dashed')
    ax.hlines(18, 0, 6, color='k', linestyles='dashed')

    ax.text(5.85, -2, '$x^*$')
    ax.text(-1.4, 17.4, '$f(x^*)$')

    ax.set_xlim((-1.2, 8))
    ax.set_ylim((-10, 20))
    ax.legend(loc='lower center', numpoints=1, frameon=False)
    ax.axis('off')

    plt.savefig('tex_notes/images/one_var.png')


def plot_two_var_ex(save=True, x_max=2):
    """Base function for plotting all countour graphs. All other contour plots
    call down to this fucntion eventually.

    Parameters
    ----------
    save : bool - save just the base contour plot?
    x_max : int - maximum value to plot in each x dimension, there are 2

    Returns
    -------
    figure, axis
    """
    def contour_function(x, y):
        return np.sin(1.3*x)*np.cos(0.9*y)+np.cos(0.8*x)*np.sin(1.9*y)+np.cos(y*0.2*x)

    x1s, x2s = np.linspace(-1, x_max, 250), np.linspace(-1, x_max, 250)
    zs = np.empty((x1s.size, x2s.size))

    for (x1, x2), _ in np.ndenumerate(zs):
        zs[x1, x2] = contour_function(x1s[x1], x2s[x2])

    arg_x2_max, arg_x1_max = np.unravel_index(zs.argmax(), zs.shape)

    fig, ax = plt.subplots(1, figsize=(4, 4))
    cs = ax.contour(x1s, x2s, zs, colors='k', levels=[0.0, 0.5, 1.0, 1.5, 1.8, 2.2, 2.4])
    ax.scatter(x1s[arg_x1_max], x2s[arg_x2_max], c='k', s=40, marker='*')

    ax.set_xticklabels([])
    ax.set_yticklabels([])

    if save:
        ax.annotate('$x^*$', xy=(x1s[arg_x1_max]-0.03, x2s[arg_x2_max]+0.05),
                    xytext=(x1s[arg_x1_max]-0.3, x2s[arg_x2_max]+0.08),
                    xycoords='data', textcoords='axes fraction',
                    arrowprops=dict(facecolor='black', shrink=0.04, width=1,
                                    headwidth=4, headlength=6),
                    horizontalalignment='right', verticalalignment='top')
        ax.clabel(cs, inline=True, fontsize=10, fmt='%1.1f')
        plt.savefig('tex_notes/images/two_var.png')

    return fig, ax


def plot_constrained_two_var_ex():
    """Plots the constraint space on top of the base contour plot. Starts
    by classing plot_two_var_ex with save = False, this turns off some of
    the annotation, and just passes back the fig and ax without saving.
    """
    fig, ax = plot_two_var_ex(False)
    ax.axhline(0, color='gray')
    ax.axvline(0, color='gray')
    ax.scatter(0.254558, 0.254558, c='k', s=30, marker='*')
    ax.plot([0, -0.254558], [0, -0.254558], 'k')
    ax.annotate('$x^*_{const}$', xy=(0.27, 0.23),  xycoords='data',
                xytext=(1.3, -0.7), textcoords='data',
                arrowprops=dict(facecolor='black', shrink=0.04, width=1,
                                headwidth=4, headlength=6),
                horizontalalignment='right', verticalalignment='top')

    ax.text(-0.254558+0.1, -0.254558, '$M$')

    circle = plt.Circle((0, 0), 0.36, color='gray')
    circle.set_alpha(0.5)
    ax.add_artist(circle)
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')

    plt.savefig('tex_notes/images/two_var_constrained.png')


def plot_gradient_two_var_ex(save=True, **kwargs):
    """Plots base contour plot with the gradient shown as an arrow coming
    perpendicular off of one of the contours.

    Parameters
    ----------
    save : bool - save just gradient contour plot?
    kwargs : potential settings to be passed along to plot_two_var_ex

    Returns
    -------
    figure, axis
    """
    fig, ax = plot_two_var_ex(False, **kwargs)
    ax.annotate('', xy=(0.2, 1.33), xytext=(0, 1.71),
                xycoords='data', textcoords='data',
                arrowprops=dict(facecolor='black', shrink=0.04, width=1,
                                headwidth=4, headlength=6),
                horizontalalignment='right', verticalalignment='top')

    if save:
        ax.text(0.15, 1.55, r'$\nabla f$')
        plt.savefig('tex_notes/images/two_var_gradient.png')

    return fig, ax

def plot_gradient_descent_two_var_ex():
    """Plots gradient descent arrows on base contour plot.
    """
    fig, ax = plot_gradient_two_var_ex(False)
    arrow_settings = [((0.43, 1.15), (0.24, 1.28), 3, 5), ((0.59, 0.99), (0.49, 1.11), 2, 4)]
    for xy, xytext, hw, hl in arrow_settings:
        ax.annotate('', xy=xy, xytext=xytext,
                    xycoords='data', textcoords='data',
                    arrowprops=dict(facecolor='black', shrink=0.04, width=1,
                                    headwidth=hw, headlength=hl),
                    horizontalalignment='right', verticalalignment='top')

    ax.scatter(0, 1.71, color='k', s=40, marker='o')
    ax.text(-0.4, 1.82, '$Start\; here$')

    plt.savefig('tex_notes/images/two_var_gradient_descent.png')


def plot_gradient_descent_multiple_ex():
    """Plots gradient descent arrows on base contour plot with axis limits
    expanded beyond the default value.
    """
    fig, ax = plot_gradient_two_var_ex(False, x_max=4)
    arrow_settings = [((0.43, 1.15), (0.24, 1.28), 3, 5), ((0.59, 0.99), (0.49, 1.11), 2, 4),
                      ((2.2, 2.68), (1.86, 2.36), 3, 5), ((2.4, 3.05), (2.25, 2.75), 2, 4)]
    for xy, xytext, hw, hl in arrow_settings:
        ax.annotate('', xy=xy, xytext=xytext,
                    xycoords='data', textcoords='data',
                    arrowprops=dict(facecolor='black', shrink=0.04, width=1,
                                    headwidth=hw, headlength=hl),
                    horizontalalignment='right', verticalalignment='top')

    plt.savefig('tex_notes/images/two_var_gradient_descent_different_starts.png')


def plot_scaling_issues_ex():
    """Plots a function with non-ideally scaled features, annotates with an arrow
    whoes length is proportional to the actual gradient, especially considering
    the scaling.
    """
    def poorly_scaled_function(x, y):
        return 8 * x**2 - 2*x*y + y**2

    x1s, x2s = np.linspace(-150, 50, 250), np.linspace(-120, 80, 250)
    zs = np.empty((x1s.size, x2s.size))

    for (x1, x2), _ in np.ndenumerate(zs):
        zs[x1, x2] = poorly_scaled_function(x1s[x1], x2s[x2])

    print(zs.min(), zs.max())

    arg_x2_max, arg_x1_max = np.unravel_index(zs.argmax(), zs.shape)

    fig, ax = plt.subplots(1, figsize=(4, 4))
    ax.contour(x1s, x2s, zs, colors='k', levels=[500, 5000, 10000, 20000, 35000,
                                                 50000, 65000, 80000, 90000, 102000,
                                                 112000, 120000, 130000])
    ax.annotate('', xy=(-117, 40),  xycoords='data',
                xytext=(-115, -81), textcoords='data',
                arrowprops=dict(facecolor='black', shrink=0.04, width=1,
                                headwidth=4, headlength=6),
                horizontalalignment='right', verticalalignment='top')
    ax.set_ylim(-100, 80)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.savefig('tex_notes/images/scaling_problems.png')


if __name__ == '__main__':
    #plot_one_var_ex()
    #plot_two_var_ex()
    #plot_constrained_two_var_ex()
    #plot_gradient_two_var_ex()
    #plot_gradient_descent_two_var_ex()
    #plot_gradient_descent_multiple_ex()
    #plot_scaling_issues_ex()

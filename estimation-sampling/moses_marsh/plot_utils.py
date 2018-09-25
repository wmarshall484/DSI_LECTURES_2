import numpy as np

def empirical_distribution(x_array, data):
    count = np.zeros(shape=len(x_array))
    for datum in data:
        count = count + (datum <= x_array)
    return count / len(data)

def one_dim_scatterplot(data, ax, jitter=0, **options):
    if jitter:
        jitter = np.random.uniform(-jitter, jitter, size=data.shape)
    else:
        jitter = np.repeat(0.0, len(data))
    ax.scatter(data, jitter, **options)
    ax.yaxis.set_ticklabels([])
    ax.set_ylim([-1, 1])

def text_in_blank_plot(text, ax):
    _ = ax.text(0.5, 0.5, text, 
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=22)
    ax.axis('off')

def superimpose_pdf_of_fit_model(data, model, ax, x_lower=-3, x_upper=3, bins=25):
    x = np.linspace(x_lower, x_upper, num=250)
    _ = ax.hist(data, bins=bins, normed=True, color="black", alpha=0.4)
    ax.plot(x, model.pdf(x), linewidth=3)

def superimpose_cdf_of_fit_model(data, model, ax, x_lower=-3, x_upper=3):
    x = np.linspace(x_lower, x_upper, num=250)
    ax.plot(x, empirical_distribution(x, data), linewidth=2)
    ax.plot(x, model.cdf(x), linewidth=2)

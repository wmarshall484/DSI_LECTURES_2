import numpy as np

def linear_model_summary(model, name=None):
    """Print a small and efficient summary of a linear model object."""
    if not name:
        name = "Linear"
    variable_names = model.params.index
    parameter_estimates = model.params
    standard_errors = model.bse
    header_string = "{:<10} {:>20} {:>15}".format("Name", "Parameter Estimate", "Standard Error")
    print("{} Model Summary".format(name).center(len(header_string)))
    print('='*len(header_string))
    print(header_string)
    print('-'*len(header_string))
    format_string = "{:<20} {:>10.2f} {:>15.2f}"
    for name, est, se in zip(variable_names, parameter_estimates, standard_errors):
        print(format_string.format(name, est, se))

def plot_arrow_from_origin(ax, x, color="black", linewidth=3):
    xlim = ax.get_xlim()
    new_xlim = [0, 0]
    new_xlim[0] = np.min([xlim[0], x[0] - 0.5])
    new_xlim[1] = np.max([xlim[1], x[0] + 0.5])
    ax.set_xlim(new_xlim)
    ylim = ax.get_ylim()
    new_ylim = [0, 0]
    new_ylim[0] = np.min([ylim[0], x[1] - 0.5])
    new_ylim[1] = np.max([ylim[1], x[1] + 0.5])
    ax.set_ylim(new_ylim)
    ax.set(aspect='equal')
    ax.arrow(0, 0, x[0], x[1],
             head_width=0.1, linewidth=linewidth, head_length=0.2,
             fc=color, ec=color, length_includes_head=True)
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

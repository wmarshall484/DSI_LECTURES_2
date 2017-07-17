# Make plots for presentation

setwd("/Users/matthew.drury/Projects/model-validation")
setwd("./R")
source("toy_model.R")
source("meta_models.R")
source("plotting_functions.R")

setwd("..")
dir.create("./plots")
setwd("./plots")


sm <- make_sinmodel(degree=1, n_train_sample=50)
smm <- fit_many_sinmodels(sm, n_to_fit=100)

p <- plot_irreducible_error()
ggsave("irreducible_error.png", width=7, height=6, p)

p <- ggplot() + area_between_true_and_linear_fit() + signal_plot() + true_linear_fit_plot()
ggsave("model_bias.png", width=7, height=6, p)

p <- ggplot() + area_between_true_and_cubic_fit() + signal_plot() + true_cubic_fit_plot()
ggsave("cubic_model_bias.png", width=7, height=6, p)

p <- ggplot() + signal_plot() + true_linear_fit_plot()
ggsave("best_linear_fit.png", width=7, height=6, p)

p <- plot_many_sinmodels(smm)
ggsave("model_variance.png", width=7, height=6, p)

# A plot of the true signal, along with a sample from X, Y
p <- ggplot() + train_data_scatter(sm) + signal_plot()
ggsave("true_signal.png", width=7, height=6, p)

# True signal and sample, along with the resulting linear regression
p <- p + fitted_plot(sm)
ggsave("single_fitted_line.png", width=7, height=6, p)

# Variance Plots
#----------------------------------------------------------------------
p <- plot_variance_of_degree()
ggsave("model_variance_standard_samples.png", width=7, height=6, p)

# Increasing the number of samples
p <- plot_variance_of_degree(n_train_sample = 200)
ggsave("model_variance_more_samples.png", width=7, height=6, p)

# Decreasing the number of samples
p <- plot_variance_of_degree(n_train_sample = 10)
ggsave("model_variance_less_samples.png", width=7, height=6, p)

# Increasing the irreducible error
p <- plot_variance_of_degree(y_std=1.5)
ggsave("model_variance_more_error.png", width=7, height=6, p)

# Decreasing the irreducible error
p <- plot_variance_of_degree(y_std=.2)
ggsave("model_variance_less_error.png", width=7, height=6, p)

# Variance of a cubic model
p <- plot_variance_of_degree(d=3)
ggsave("model_variance_cubic.png", width=7, height=6, p)

# Variance of a quartic model
p <- plot_variance_of_degree(d=5)
ggsave("model_variance_quartic.png", width=7, height=6, p)

# Variance of a septic
p <- plot_variance_of_degree(d=7)
ggsave("model_variance_septic.png", width=7, height=6, p)

# Plot of learning curves on out of sample data
p <- (ggplot() + plot_learning_curve_data(1, seq(10, 150, 5))
               + plot_learning_curve_data(3, seq(10, 150, 5), alpha=.8)
               + plot_learning_curve_data(5, seq(10, 150, 5), alpha=.6)
               + plot_learning_curve_data(7, seq(10, 150, 5), alpha=.4)
               + scale_y_continuous(limits=c(.5, 1.25))
  )
ggsave("out_of_sample_learning_curves.png", width=7, height=6, p)


# Plot of learning curves on in sample data
p <- (ggplot() + plot_learning_curve_data(1, seq(10, 150, 5), train_data=TRUE)
      + plot_learning_curve_data(3, seq(10, 150, 5), alpha=.8, train_data=TRUE)
      + plot_learning_curve_data(5, seq(10, 150, 5), alpha=.6, train_data=TRUE)
      + plot_learning_curve_data(7, seq(10, 150, 5), alpha=.4, train_data=TRUE)
)
ggsave("in_sample_learning_curves.png", width=7, height=6, p)

p <- (ggplot() + plot_learning_curve_data(5, seq(10, 300, 5), train_data=TRUE)
        + plot_learning_curve_data(5, seq(10, 300, 5))
        + scale_y_continuous(limits=c(0, 1.25))
)

# Training vs. testing error for various degrees
p <- ggplot() + plot_learning_curve_degree(1:8)
ggsave("learning_curves_by_degree.png", width=7, height=6, p)


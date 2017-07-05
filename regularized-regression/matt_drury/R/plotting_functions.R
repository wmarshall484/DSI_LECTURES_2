plot_many_sinmodels <- function(many_sinmodels, plot_line=TRUE) {
  p <- ggplot() + signal_plot()
  for(model in many_sinmodels) p <- p + fitted_plot(model, alpha=.2)
  if(plot_line) {
    p <- p  + true_linear_fit_plot()
  }
  p
}

plot_irreducible_error <- function() {
  e <- sin(1.5) + rnorm(100, 0, .5)
  d <- data.frame(X=rep(1.5, 100), Y=e)
  ggplot() + signal_plot() + geom_point(data=d, aes(x=X, y=Y), alpha=.25)
}

plot_variance_of_degree <- function(d=1, n_train_sample=50, n_to_fit=100, y_std = .75) {
  sm <- make_sinmodel(degree=d, y_std=y_std, n_train_sample=n_train_sample)
  smm <- fit_many_sinmodels(sm, n_to_fit=n_to_fit)
  p <- plot_many_sinmodels(smm, plot_line=FALSE) + train_data_scatter(sm, alpha=.25)
  p
}

plot_learning_curve_data <- function(degree, n_obs_in_train, alpha=1, test_data=NULL, train_data=FALSE) {
  if(is.null(test_data)) test_data <- sample_XY(n_samples=500)
  out_of_sample_errors <- score_fit_models_on_varying_amounts_of_data(
    degree=degree, n_obs=n_obs_in_train, test_data, train_data
  )
  plot_df <- data.frame(
    n_training_points=as.numeric(names(out_of_sample_errors)),
    avg_sum_of_squared_error=unlist(out_of_sample_errors),
    degree=degree
  )
  geom_line(data=plot_df, aes(x=n_training_points, y=avg_sum_of_squared_error, color=degree), alpha=alpha)
}

make_learning_curve_df <- function(plot_df_train, plot_df_test, do_train, do_test) {
  if(do_train && do_test) {
    rbind(plot_df_train, plot_df_test)
  } else if(do_train) {
    plot_df_train
  } else if(do_test) {
    plot_df_test
  }
}

plot_learning_curve_degree <- function(degrees, alpha=1, test_data=NULL, do_train=TRUE, do_test=TRUE) {
  if(is.null(test_data)) test_data <- sample_XY(n_samples=500)
  out_of_sample_errors <- score_fit_models_of_varying_degree(
    degrees=degrees, test_data, train_data=FALSE
  )
  in_sample_errors <- score_fit_models_of_varying_degree(
    degrees=degrees, train_data=TRUE
  )
  plot_df_train <- data.frame(
    polynomial_degree=as.numeric(names(in_sample_errors)),
    avg_sum_of_squared_error=unlist(in_sample_errors),
    type="In Sample"
  )
  plot_df_test<- data.frame(
    polynomial_degree=as.numeric(names(out_of_sample_errors)),
    avg_sum_of_squared_error=unlist(out_of_sample_errors),
    type="Out Of Sample"
  )
  plot_df <- make_learning_curve_df(plot_df_train, plot_df_test, do_train, do_test)
  #print(plot_df)
  geom_line(data=plot_df, aes(x=polynomial_degree, y=avg_sum_of_squared_error, color=type, group=type), alpha=alpha)
}
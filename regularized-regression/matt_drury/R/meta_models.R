fit_many_sinmodels <- function(obj, n_to_fit) {
  models <- list()
  for(i in 1:n_to_fit) {
    models[[i]] <- make_sinmodel(n_train_sample=obj$n_train_sample, y_std=obj$y_std, degree=obj$degree)
  }
  models
}

fit_models_of_varying_degree <-function(degrees) {
  models <- list()
  for(d in degrees) {
    model <- make_sinmodel(n_train_samples=50, degree=d)
    models[[as.character(d)]] <- fit_many_sinmodels(model, 500)
  }
  models
}

fit_models_on_varying_amounts_of_data <- function(degree, n_obs) {
  models <- list()
  for(n in n_obs) {
    model <- make_sinmodel(n_train_samples=n, degree=degree)
    models[[as.character(n)]] <- fit_many_sinmodels(model, 100)
  }
  models
}

.reduce_models_to_scores <- function(models, data, train_data) {
  if(train_data) {
    lapply(models, function(m) {
      sum_of_squared_errors(m, newdata=m$X, newresponse=m$Y)
    })
  } else {
    lapply(models, function(m) {
      sum_of_squared_errors(m, newdata=data$X, newresponse=data$Y)
    })
  }
}

score_fit_models_on_varying_amounts_of_data <- function(degree, n_obs, data=NULL, train_data=FALSE) {
  models_by_n_obs <- fit_models_on_varying_amounts_of_data(degree, n_obs)
  model_scores <- list()
  for(models in models_by_n_obs) {
    key <- as.character(length(models[[1]]$Y))
    model_scores[[key]] <- .reduce_models_to_scores(models, data, train_data)
  }
  avg_model_scores <- lapply(model_scores, function(ms) {mean(unlist(ms))})
  avg_model_scores
}

score_fit_models_of_varying_degree <- function(degrees, data=NULL, train_data=FALSE) {
  models_by_degree <- fit_models_of_varying_degree(degrees)
  model_scores <- list()
  for(models in models_by_degree) {
    key <- as.character(models[[1]]$degree)
    model_scores[[key]] <- .reduce_models_to_scores(models, data, train_data)
  }
  avg_model_scores <- lapply(model_scores, function(ms) {mean(unlist(ms))})
  avg_model_scores
}

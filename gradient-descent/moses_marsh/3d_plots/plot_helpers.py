import numpy as np
from sklearn.datasets import make_regression
from scipy.spatial.distance import norm
from itertools import product
from collections import OrderedDict
from plotly.graph_objs import *
import plotly.tools as tls
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode()
import time

def gradient_descent(X, y, 
                     cost_function, gradient_of_cost_function, 
                     initial_guess, learning_rate=.1, 
                     threshold=1e-3, max_iter=1e3):
    params = initial_guess
    param_history = [(initial_guess[0], initial_guess[1], cost_function(X, y, params))]
    improvement = threshold
    old_cost = 100000
    iterations = 0
    time_history = [time.time()]
    while (norm(gradient_of_cost_function(X, y, params)) >= threshold 
           and iterations < max_iter):
        iterations += 1
        params -= learning_rate*gradient_of_cost_function(X, y, params)
        cost = cost_function(X, y, params)
        param_history.append((params[0], params[1], cost)) # for plotting
        improvement = np.abs(cost - old_cost)/old_cost
        old_cost = cost
        time_history.append(time.time())
    if iterations == max_iter:
        print("max iterations reached")
    print("Final gradient of cost function {}".format(gradient_of_cost_function(X, y, params)))
    print("Final params {}".format(params))
    return param_history, time_history

def stochastic_gradient_descent(X, y, 
                     cost_function, gradient_of_cost_function, 
                     initial_guess, learning_rate=.1, 
                     threshold=1e-3, max_iter=1e3, batch_size=1):
    batch_size = min(batch_size, X.shape[0])
    params = initial_guess
    param_history = [(initial_guess[0], initial_guess[1])]
    improvement = threshold
    old_cost = 100000
    iterations = 0
    time_history = [time.time()]
    while (norm(gradient_of_cost_function(X, y, params)) >= threshold 
           and iterations < max_iter):
        # select indices of mini-batch
        min_index = batch_size*iterations % X.shape[0]
        indices = []
        while len(indices) < batch_size:
            indices.append((min_index + len(indices)) % X.shape[0])
        Xi, yi = X[indices], y[indices]
        # update parameters
        params -= learning_rate*gradient_of_cost_function(Xi, yi, params)
        cost = cost_function(Xi, yi, params)
        param_history.append((params[0], params[1])) # for plotting
        improvement = np.abs(cost - old_cost)/old_cost
        old_cost = cost
        iterations += 1
        time_history.append(time.time())
    if iterations == max_iter:
        print("max iterations reached")
    print("Final gradient of cost function {}".format(gradient_of_cost_function(X, y, params)))
    print("Final params {}".format(params))
    return param_history, time_history

def plot_results(X, y, cost_function, param_history):
    params = param_history[-1][0:2]
    x_params = np.array([params[0] - (params[0]-p[0]) for p in param_history] +
                [params[0] + (params[0]-p[0]) for p in param_history])
    x_params.sort()
    y_params = np.array([params[1] - (params[1]-p[1]) for p in param_history] +
                [params[1] + (params[1]-p[1]) for p in param_history])
    y_params.sort()
    samples = list(product(x_params, y_params))
    costs = [cost_function(X, y, np.array([p[0], p[1]])) for p in samples]
    costs = np.reshape(costs, (len(x_params), -1))
    cost_surface = Surface(
        x = x_params,
        y = y_params,
        z = costs,
        colorscale = [[0, 'rgb(31,119,180)'], 
                      [0.5, 'rgb(143, 123, 196)'], 
                      [1, 'rgb(255,127,97)']],
        name='Cost Function'
    )
    param_history = Scatter3d(
        x = x_params,
        y = y_params,
        z = [p[2] for p in param_history],
        mode = 'lines+markers'
    )
    data_3d_plot = Data([cost_surface, param_history])
    layout = Layout(
        scene = dict(
            xaxis = dict(title='beta0'),
            yaxis = dict(title='beta1'),
            zaxis = dict(title='cost')
            ))
    figure_3d = Figure(data=data_3d_plot, layout=layout)
    return figure_3d

def plot_sgd_results(X, y, cost_function, param_history):
    x_history = [p[0] for p in param_history]
    y_history = [p[1] for p in param_history]
    x_params = np.linspace(min(x_history),
                           max(x_history),
                           100)
    y_params = np.linspace(min(y_history),
                           max(y_history),
                           100)
    samples = list(product(x_params, y_params))
    demo_points = OrderedDict()
    for p in param_history:
        best_sample = samples[0]
        min_distance = ((p[0]-best_sample[0])**2+(p[1]-best_sample[1])**2)**.5
        for sample in samples:
            d = ((p[0]-sample[0])**2+(p[1]-sample[1])**2)**.5
            if d < min_distance:
                best_sample = sample
                min_distance = d
        demo_points[tuple(p)] = best_sample
    costs = [cost_function(X, y, np.array([p[0], p[1]])) for p in samples]
    costs = np.reshape(costs, (len(x_params), -1))
    cost_surface = Surface(
        x = x_params,
        y = y_params,
        z = costs,
        colorscale = [[0, 'rgb(31,119,180)'], 
                      [0.5, 'rgb(143, 123, 196)'], 
                      [1, 'rgb(255,127,97)']],
        name='Cost Function'
    )
    param_history = Scatter3d(
        x = [d[0] for d in demo_points],
        y = [d[1] for d in demo_points],
        z = [cost_function(X, y, d) for d in demo_points],
        mode = 'lines+markers'
    )
    data_3d_plot = Data([cost_surface, param_history])
    layout = Layout(
        scene = dict(
            xaxis = dict(title='beta0'),
            yaxis = dict(title='beta1'),
            zaxis = dict(title='cost')
            ))
    figure_3d = Figure(data=data_3d_plot, layout=layout)
    return figure_3d

def predict(X, params):
    y_predicted = X.dot(params)
    return y_predicted

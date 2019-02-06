import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.io import output_notebook, show, output_file
from bokeh.models import ColumnDataSource, HoverTool, Panel
from bokeh.models.widgets import Tabs

class BokehHistogram():
    '''
    A class to simplify the making of interactive histograms with the Bokeh library.
    Requires: Bokeh, Pandas, and Numpy.
    '''

    def __init__(self, colors=["SteelBlue", "Tan"], height=600, width=600):
        self.colors = colors
        self.height = height
        self.width = width

    def hist_hover(self, dataframe, column, bins=30, log_scale=False, show_plot=True):
        """
        A method for creating a sinlge Bokeh histogram with hovertool interactivity.

        Parameters:
        ----------
        Input:
        dataframe {df}: Pandas dataframe
        column {string}: column of dataframe to plot in histogram
        bins {int}: number of bins in histogram
        log_scale {bool}: True to plot on a log scale
        colors {list -> string}: list of colors for histogram; first color default color, second color is hover color
        show_plot {bool}: True to display the plot, False to store the plot in a variable (for use in later methods)

        Output:
        plot: bokeh historgram with interactive hover tool

        """
        # build histogram data with Numpy
        hist, edges = np.histogram(dataframe[column], bins = bins)
        hist_df = pd.DataFrame({column: hist,
                                 "left": edges[:-1],
                                 "right": edges[1:]})
        hist_df["interval"] = ["%d to %d" % (left, right) for left, 
                               right in zip(hist_df["left"], hist_df["right"])]
        # bokeh histogram with hover tool
        if log_scale == True:
            hist_df["log"] = np.log(hist_df[column])
            src = ColumnDataSource(hist_df)
            plot = figure(plot_height = self.height, plot_width = self.width,
                  title = "Histogram of {}".format(column.capitalize()),
                  x_axis_label = column.capitalize(),
                  y_axis_label = "Log Count")    
            plot.quad(bottom = 0, top = "log",left = "left", 
                right = "right", source = src, fill_color = self.colors[0], 
                line_color = "black", fill_alpha = 0.7,
                hover_fill_alpha = 1.0, hover_fill_color = self.colors[1])
        else:
            src = ColumnDataSource(hist_df)
            plot = figure(plot_height = self.height, plot_width = self.width,
                  title = "Histogram of {}".format(column.capitalize()),
                  x_axis_label = column.capitalize(),
                  y_axis_label = "Count")    
            plot.quad(bottom = 0, top = column,left = "left", 
                right = "right", source = src, fill_color = self.colors[0], 
                line_color = "black", fill_alpha = 0.7,
                hover_fill_alpha = 1.0, hover_fill_color = self.colors[1])

        # hover tool
        hover = HoverTool(tooltips = [('Interval', '@interval'),
                                  ('Count', str("@" + column))])
        plot.add_tools(hover)

        # output
        if show_plot == True:
            show(plot)
        else:
            return plot

    def histotabs(self, dataframe, features, log_scale=False, show_plot=False):
        '''
        Builds tabbed interface for a series of histograms; calls hist_hover. Specifying 'show_plot=True' will simply display the histograms in sequence rather than in a tabbed interface.

        Parameters:
        ----------
        Input:
        dataframe {df}: a Pandas dataframe
        features {list -> string}: list of features to plot
        log_scale {bool}: True to plot on a log scale
        colors {list -> string}: list of colors for histogram; first color default color, second color is hover color
        show_plot {bool}: True to display the plot, False to store the plot in a variable (for use in later methods)

        Output:
        Tabbed interface for viewing interactive histograms of specified features

        '''
        hists = []
        for f in features:
            h = self.hist_hover(dataframe, f, log_scale=log_scale, show_plot=show_plot)
            p = Panel(child=h, title=f.capitalize())
            hists.append(p)
        t = Tabs(tabs=hists)
        show(t)

    def filtered_histotabs(self, dataframe, feature, filter_feature, log_scale=False, show_plot=False):
        '''
        Builds tabbed histogram interface for one feature filtered by another. Feature is numeric, fiter feature is categorical.

        Parameters:
        ----------
        Input:
        dataframe {df}: a Pandas dataframe
        features {list -> string}: list of features to plot
        log_scale {bool}: True to plot on a log scale
        colors {list -> string}: list of colors for histogram; first color default color, second color is hover color
        show_plot {bool}: True to display the plot, False to store the plot in a variable (for use in later methods)

        Output:
        Tabbed interface for viewing interactive histograms of specified feature filtered by categorical filter feature

        '''
        hists = []
        for col in dataframe[filter_feature].unique():
            sub_df = dataframe[dataframe[filter_feature] == col]
            histo = self.hist_hover(sub_df, feature, log_scale=log_scale, show_plot=show_plot)
            p = Panel(child = histo, title=col)
            hists.append(p)
        t = Tabs(tabs=hists)
        show(t)

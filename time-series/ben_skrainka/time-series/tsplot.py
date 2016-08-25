
import matplotlib.pyplot as plt
import statsmodels.api as sm

def tsplot(data, lags=28):
    fig = plt.figure(figsize=(15,10))
    ax1 = fig.add_subplot(311)
    ax1.plot(data)
    ax1.set_title('y_t vs. t')
    ax2 = fig.add_subplot(312)
    sm.graphics.tsa.plot_acf(data, lags=lags, ax=ax2)
    ax3 = fig.add_subplot(313)
    sm.graphics.tsa.plot_pacf(data, lags=lags, ax=ax3)
    fig.show()
    return fig

import matplotlib.pyplot as plt
import numpy as np

class VectorPlotter():
    def __init__(self,**kwargs):
        self._figsize = kwargs.get('figsize', [5,5])
        self._limits = kwargs.get('limits', [-5,5])
        self.fig = plt.figure(figsize=self._figsize)
        self.ax = plt.axes()

    def plot_vector(self, u, **kwargs):
        if isinstance(u,np.ndarray):
            u = u.ravel()
        orig = kwargs.get('orig', [0,0])
        if isinstance(orig,np.ndarray):
            orig = orig.ravel()

        _color = kwargs.get('color', )
        self.ax.arrow(orig[0], orig[1], u[0], u[1],
                        head_width=0.2, head_length=0.2,
                        fc=_color, ec=_color)

    def plot_dotproduct(self, u, **kwargs):
        # make these smaller to increase the resolution
        dx, dy = 0.1, 0.1

        if isinstance(u,np.ndarray):
            u = u.ravel()

        # generate 2 2d grids for the x & y bounds
        y, x = np.mgrid[slice(self._limits[0], self._limits[1] + dy, dy),
                        slice(self._limits[0], self._limits[1] + dx, dx)]

        z = x * u[0] + y * u[1]

        # x and y are bounds, so z should be the value *inside* those bounds.
        # Therefore, remove the last value from the z array.
        z = z[:-1, :-1]
        z_min, z_max = -np.abs(z).max(), np.abs(z).max()

        #plt.figure(figsize=(6,5))
        plt.pcolor(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
        plt.title('dot product')

        # set the limits of the plot to the limits of the data
        ax = plt.axes()
        ax.arrow(0, 0, u[0], u[1],
                                head_width=0.2, head_length=0.2,
                                fc='k', ec='k')

        plt.axis([x.min(), x.max(), y.min(), y.max()])
        plt.colorbar()
        plt.show()

    def show(self):
        self.ax.grid(True)
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['top'].set_color('none')
        self.ax.set_xlim(self._limits)
        self.ax.set_ylim(self._limits)
        plt.show()

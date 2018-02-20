This is all setup on the Galvanize DSI workstations, but if you'd like to use your home computer, you can install all the same packages.

#### Step 1: Install Anaconda

We will be using [Anaconda](https://www.anaconda.com/download) with Python version 3.6. Download the command line installer (the one ending in `.sh`). Install this by navigating to the directory containing the file in your terminal and typing `bash name_of_anaconda_installer.sh` (for example, `Anaconda3-5.1.0-MacOSX-x86_64.sh`). Say yes to all the prompts. Once Anaconda is installed, you will have Python along with several useful packages and programs:

* NumPy
* SciPy
* Pandas
* statsmodels
* MatPlotLib
* IPython
* nose
* pep8

You can see the [full list of packages](https://docs.anaconda.com/anaconda/packages/pkg-docs) if you are so inclined.

You can use [conda](https://www.anaconda.com/blog/developer-blog/conda-data-science/) or pip to install any packages that are not included like this:

```
pip install flask
```

#### Step 2: Install Atom

We will use Atom for editing (If you have mastered `vim` or `emacs`, there is no need to switch). When you are working alone, you are welcome to use any editor you'd like. You can download [Atom](https://atom.io) for free, or install via `brew`:

```
brew cask install atom

```

<h1>Spark Demos </h1>

<h2>TLDR;</h2>
Spark is a distributed computing platform that has a python API.  For people accustomed to python programing, there are analogous functions such as map, filter, and sort.  The quickest way to get started is to grab a Spark 2.0 docker image attached to a Jupyter notebook, which you can find here: https://hub.docker.com/r/ezamir/jupyter-spark-2.0/

<h2>Background</h2>
Spark is an open sourced platform for distributed computation.  Originally written in scala, it has API's for scala, java, R, and of course, python.  You can read more on the Spark website http://spark.apache.org/

<h2>Getting Started</h2>
The first step is to get spark working on your machine locally.  It should go without saying that Sparks primary purpose is not to be run on a single machine.  With that said, one can explore many features by small scale experimentation.  There are two options for running locally.
<h3>Spark/Jupyter Docker image</h3>
There is a docker image that has all the instructions for getting up and running really quickly.  https://hub.docker.com/r/ezamir/jupyter-spark-2.0/ .  This is the quickest way to get started, but does require you to be comfortable with docker (if not, no time like the present to learn!)

<h3>Install locally</h3>
Alternatively, you can install spark locally.  Mac users might be able to use homebrew: `brew install apache-spark` (disclaimer, I've only used the more manual process described below).

Alternatively, download the latest greatest version of Spark.  It is totally free and can be aquired at http://spark.apache.org/downloads.html

For these demos, I used Spark 2.0.2, Pre-built for Hadoop 2.7 (N.B. for local installations, the hadoop version shouldn't matter').

Once you download the package, unpack the archive, and move the directory somewhere you will remember it (I used ~/).  Then add ~/spark-[spark version here]/bin to your path variable.  If you type `pyspark`, after a little bit of loading, you should have a command propt.  You can either use the shell, or if you want to use Jupyter notebooks, you can simply execute the `nb_start script`.

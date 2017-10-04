# Matt's Graph Lecture

Discussion of Graphs and Networks.

## Objectives

### Morning

- Discuss examples of graphs found in real life.
- Formally define a graph.
- Discuss two ways to represent a graph as a simple data structure.
- Draw the graph represented by a simple data structure.
- Define and illustrate the basic concepts in a graph
  - degree
  - path
  - connected and disconnected graph
- Define and illustrate a tree
- Whiteboard some pseudocode for the breadth first search algorithm.

## Afternoon

- Define centrality measures of vertices
  - Degree Centrality
  - Betweenness Centrality
  - Eigenvector Centrality
- Discuss the connection between communities in graphs and clusters in scatterplots
- Discuss the modularity measure of a graph partition into communities
- Whiteboard the Grivan-Newman algorithm for partitioning a graph into communities.

## Installs

Assuming that you are using Anaconda, you should already have `networkx` (the main graph library in python).  This lecture assumes you are running `networkx` version 2.0 (you can check by importing networkx and running `nextworkx.__version__`).  If your install is out of data, run `pip install networkx --upgrade`.

I'll also be using the following libraries to help out:

```
brew install graphviz
pip install community
pip install nxpd
```

Additionally, there is some helper code in `GraphTools.py` that I've written that I will use throughout the day.

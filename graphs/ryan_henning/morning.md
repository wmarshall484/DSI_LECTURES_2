## Graph Theory Lecture

These are my very rough lecture notes for the Graph Theory day.

#### Whiteboard portion

I begin on the whiteboard. See my [hand-written notes](graphs_notes_color.pdf).

Before lecture, I draw four example graphs on the board (from pages 1-2 of my notes).

The beginning of my lecture is introducing graphs (shocking, I know). I begin by talking about what a graph is. It is nodes and edges. What's a node? What's an edge? This is cool. We can represent many different concepts with this nodes & edges (graphs) framework.

I point at my four example graphs which are drawn on the board. "Here are four things we can use graphs to represent. First, cities & roads. Second, Facebook friends. Third, Twitter followers. Forth, website & links."

I now introduce the terms "directed / undirected" and "weighted / unweighted". My four example graphs show the four combinations of these. I point that out and write on the board what they are (e.g. directed & unweighted).

Now define a graph formally. It's a set of nodes and a set of edges.

Now go through a bunch of terminology: vertex (node), edge (connection), neighbor, degree, ... etc. See my notes for all the terms.

Now I motivate why we call it Graph _Theory_. Talk about the first graph _theory_ by Euler in 1736 about Euler Paths and Euler Circuits.

Now I talk about modern Graph Theory. Specifically I talk about TSP and super-briefly about NP-hard problems as an open area of research.

Now... let's talk about easier problems we CAN solve quickly. We have precise questions we can ask (see notes), and we have ambiguous questions we can ask (see notes).

This is all well and good, but how do we represent a graph in memory? There are two common ways: adjacency lists and adjacency matrices. Btw, the term "adjacency list" is a little misleading--you will really use dictionaries in python. The term "adjacency matrix" is spot on though. Draw on the board how these look (see notes).

#### Live-coding portion

Work through whichever functions you find interesting. You will not have time for all of them. [graph_demo.py](graph_demo.py) contains stubbed out stuff for you to fill in during class. [graph.py](graph.py) contains the solutions.

HIGHLIGHT THAT ALL THESE ARE VERY PRECISE PROBLEM STATEMENTS WITH PRECISE ALGORITHMS. We will cover the more data-sciency, ambiguous questions during the afternoon.


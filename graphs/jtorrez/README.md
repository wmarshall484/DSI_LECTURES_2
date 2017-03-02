# Graphs (Network Analysis)

## Credit
This majority of this lecture was created by Matt Drury and the original version can be found [here](http://www.sci.unich.it/~francesc/teaching/network/eigenvector.html).

## Modifications

The changes between Matt's original lecture and this one are as follows:

1. Added both morning and afternoon objectives.
  * The split between morning and afternoon lectures is different than Matt's lecture to better reflect the exercises.
2. Added comments to import statements to indicate their origin (since one of the standards is to know how to use the standard Python graph libraries)
3. Added installation instructions for some of the tools and modules that students will likely not have.
4. Added information about depth first search (DFS) and notes about stacks vs. queues.
5. Added example of using Girvan-Newmann algorithm with visualization of the graph as it changes.

## Emphases

This lecture goes more in-depth into the search algorithms and data structures as these are more generalizable knowledge and students likely will be asked about them in interviews.

## Post-lecture observations

* The most difficult parts of the lecture for the students were eigenvector centrality and modularity. Emphasizing the conceptual meaning of these terms (eigenvector centrality: you are important if your friends are also important, modularity: the communities in this graph are most densely connected than I would expect at random) seemed to help the students leave the classroom happy.

* I edited the search algorithms section to use the term traversal instead of search because many students were having issues understanding why there was no stopping criteria for the "search" algorithms.

* Added a link to the Susan Early's slides about modularity ([here](https://github.com/zipfian/DSI_Lectures/blob/master/graphs/s_eraly/afternoon_lecture.pdf)) which I used to supplement the end of my lecture.

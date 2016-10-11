# MapReduce Lecture

### Slides

See [Cary Goltermann's slides](../cary_goltermann/).

### Notes & Code Demo

[MapReduce](https://en.wikipedia.org/wiki/MapReduce) is a parallel programming model. The most popular library which implements MapReduce is [Hadoop](http://hadoop.apache.org/), but that's not the only implementation of MapReduce! To prove this, let's do some MapReduce stuff inside MongoDB.

Load the `clicks` data from [this exercise](https://github.com/zipfian/web-scraping/blob/master/individual.md). Run this code to compute the number of _clicks_ for each city:

```
use clicks

db.log.mapReduce(
  function() {
    emit(this.cy, 1)
  },
  function(key, values) {
    return Array.sum(values)
  },
  {
    query: {'cy': {'$exists': true}},
    out: 'city_count'
  }
)

db.city_count.find()

db.city_count.find({"_id": "San Francisco"})
```

Load the `nyt_dump` data from [this exercise](https://github.com/zipfian/nlp/blob/master/individual.md). Run this code to do a bag-of-words on the NYT articles:

```
use nyt_dump

db.articles.mapReduce(
  function() {
    for (i = 0; i < this.content.length; i++) {
      splt = this.content[i].toLowerCase().split(/\s+/)
      for (j = 0; j < splt.length; j++) {
        emit(splt[j], 1)
      }
    }
  },
  function(key, values) {
    return Array.sum(values)
  },
  {
    query: {'content': {'$exists': true}},
    out: 'word_counts'
  }
)

db.word_counts.find({'_id': /^lett.+/})
```

Okay, that's cool, but now let's **not** use MongoDB (which makes us write in Javascript). Let's write Python!

The Hadoop library is all written in Java, but there's a great Python library named [MRJob](https://github.com/Yelp/mrjob) which lets your write Hadoop MapReduce jobs _in Python_. Yay!

MRJob makes writing MapReduce jobs pretty easy. Combine that with how powerful the MapReduce programming model is, plus the ability to launch a cluster on AWS and pay by-the-hour, and we can see we are in a very good situation. :) Here's a quote from the book _[Data-Intensive Text Processing with MapReduce](http://lintool.github.io/MapReduceAlgorithms/MapReduce-book-final.pdf)_ by Jimmy Lin and Chris Dyer (top of page 16):
> Anyone can download the open source Hadoop implementation of MapReduce, pay a modest fee to rent a cluster from a utility cloud provider, and be happily processing terabytes upon terabytes of data within the week.

So, let's write a MapReduce in Python using MRJob, and let's talk about what it's doing. Run the code with `python word_counter.py data/sample_documents.txt`

```python
"""
The classic MapReduce job: count the frequency of words.
"""

from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def reducer(self, word, counts):
        yield (word, sum(counts))

if __name__ == '__main__':
     MRWordFreqCount.run()
```

**END OF MORNING LESSON**

Let's do _some_ relational algebra with MapReduce. Recall, SQL implements the relational algebra concepts, so essentially we are learning how to do SQL things with MapReduce.

**Union**

Run the code with `python union.py data/words_*.txt`

```python
"""
How to do a union (from relational algebra) using MapReduce.
"""

from mrjob.job import MRJob

class UnionJob(MRJob):

    def mapper(self, _, line):
        yield (line, 0)

    def reducer(self, key, values):
        yield (key, None)

if __name__ == '__main__':
     UnionJob.run()
```

**Intersection**

Run the code with `python intersection.py data/words_*.txt`

```python
"""
How to do a intersection (from relational algebra) using MapReduce.
"""

from mrjob.job import MRJob

class IntersectionJob(MRJob):

    def mapper(self, _, line):
        yield (line, 0)

    def reducer(self, key, values):
        if len(list(values)) >= 2:
            yield (key, None)

if __name__ == '__main__':
     IntersectionJob.run()
```

**Difference**

Run the code with `python difference.py data/words_*.txt`

```python
"""
How to do a difference (from relational algebra) using MapReduce.
"""

import os
from mrjob.job import MRJob

class DifferenceJob(MRJob):

    def mapper(self, _, line):
        file_path = os.environ['map_input_file']
        yield (line, '1' in file_path)

    def reducer(self, key, values):
        values = list(values)
        if values == [1]:
            yield (key, None)

if __name__ == '__main__':
     DifferenceJob.run()
```

**Selection**

Run the code with `python selection.py data/golf_features.csv`

```python
"""
How to do a selection (from relational algebra) using MapReduce.
"""

from mrjob.job import MRJob

class SelectionJob(MRJob):

    def mapper(self, _, line):
        date, outlook, temperature, humidity, windy = line.split(',')
        if outlook == 'sunny':
            yield ((date, outlook, temperature, humidity, windy), 0)

    def reducer(self, key, values):
        yield key, None

if __name__ == '__main__':
     SelectionJob.run()
```

**Projection**

Run the code with `python projection.py data/golf_features.csv`

```python
"""
How to do a projection (from relational algebra) using MapReduce.
"""

from mrjob.job import MRJob

class ProjectionJob(MRJob):

    def mapper(self, _, line):
        date, outlook, temperature, humidity, windy = line.split(',')
        yield ((date, outlook), 0)

    def reducer(self, key, values):
        yield (key, None)

if __name__ == '__main__':
     ProjectionJob.run()
```

**Grouping / Aggregation**

Run the code with `python groupby.py data/golf_features.csv`

```python
"""
How to do a group-by / aggregation (from relational algebra) using MapReduce.
"""

import numpy as np
from mrjob.job import MRJob

class GroupByJob(MRJob):

    def mapper(self, _, line):
        date, outlook, temperature, humidity, windy = line.split(',')
        yield (outlook, float(temperature))

    def reducer(self, key, values):
        yield (key, np.mean(list(values)))

if __name__ == '__main__':
     GroupByJob.run()
```

**Join**

Run the code with `python join.py data/golf_*.csv`

```python
"""
How to do a join (from relational algebra) using MapReduce.
"""

import os
from itertools import product
from mrjob.job import MRJob

class JoinJob(MRJob):

    def mapper(self, _, line):
        file_path    = os.environ['map_input_file']
        parts        = line.split(',')
        join_on      = parts[0]
        other_values = parts[1:]
        yield (join_on, (file_path, other_values))

    def reducer(self, key, values):
        values = list(values)
        file_paths = list(set([v[0] for v in values]))
        if len(file_paths) < 2:
            return  # no match-up between the two relations
        if len(file_paths) > 2:
            raise Exception('A join must operate on exactly two relations.')
        left_values  = [v[1] for v in values if v[0] == file_paths[0]]
        right_values = [v[1] for v in values if v[0] == file_paths[1]]
        for l, r in product(left_values, right_values):
            yield (key, l + r)

if __name__ == '__main__':
     JoinJob.run()
```

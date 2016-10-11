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

Let's do relational algebra with MapReduce. Recall, SQL implements all those relational algebra concepts, so essentially we are learning how to do SQL things with MapReduce.

**Selection**

```python

```

**Projection**

**Union**

**Intersection**

**Join**

**Grouping / Aggregation**

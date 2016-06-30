
    %%javascript
    $.getScript('http://asimjalis.github.io/ipyn-ext/js/ipyn-present.js')

<!-- 
The ipynb was auto-generated from markdown using notedown.
Instead of modifying the ipynb file modify the markdown source. 
-->

<h1 class="tocheading">Spark</h1>
<div id="toc"></div>

<img src="images/spark-logo.png">

Apache Spark
============

Spark Intro
-----------

What is Spark?

- Spark is a framework for distributed processing.

- It is a streamlined alternative to Map-Reduce.

- Spark applications can be written in Python, Scala, or Java.

Why Spark
---------

Why learn Spark?

- Spark enables you to analyze petabytes of data.

- Spark skills are in high demand--<http://indeed.com/salary>.

- Spark is signficantly faster than MapReduce.

- Paradoxically, Spark's API is simpler than the MapReduce API.

Goals
-----

By the end of this lecture, you will be able to:

- Create RDDs to distribute data across a cluster

- Use the Spark shell to compose and execute Spark commands

- Use Spark to analyze stock market data

Spark Version History
---------------------

Date               |Version        |Changes
----               |-------        |-------
May 30, 2014       |Spark 1.0.0    |APIs stabilized 
September 11, 2014 |Spark 1.1.0    |New functions in MLlib, Spark SQL
December 18, 2014  |Spark 1.2.0    |Python Streaming API and better streaming fault tolerance
March 13, 2015     |Spark 1.3.0    |DataFrame API, Kafka integration in Streaming
April 17, 2015     |Spark 1.3.1    |Bug fixes, minor changes

Matei Zaharia
-------------

<img style="width:50%" src="images/matei.jpg">

Essense of Spark
----------------

What is the basic idea of Spark?

- Spark takes the Map-Reduce paradigm and changes it in some critical
  ways.

- Instead of writing single Map-Reduce jobs a Spark job consists of a
  series of map and reduce functions. 
  
- However, the intermediate data is kept in memory instead of being
  written to disk or written to HDFS.

Pop Quiz
--------

<details><summary>
Q: Since Spark keeps intermediate data in memory to get speed, what
does it make us give up? Where's the catch?
</summary>
1. Spark does a trade-off between memory and performance.
<br>
2. While Spark apps are faster, they also consume more memory.
<br>
3. Spark outshines Map-Reduce in iterative algorithms where the
   overhead of saving the results of each step to HDFS slows down
   Map-Reduce.
<br>
4. For non-iterative algorithms Spark is comparable to Map-Reduce.
</details>

Spark Logging
-------------

Q: How can I make Spark logging less verbose?

- By default Spark logs messages at the `INFO` level.

- Here are the steps to make it only print out warnings and errors.

```sh
cd $SPARK_HOME/conf
cp log4j.properties.template log4j.properties
```

- Edit `log4j.properties` and replace `rootCategory=INFO` with `rootCategory=ERROR`

Spark Fundamentals
==================

Spark Execution
---------------

<img src="images/spark-cluster.png">


Spark Terminology
-----------------

Term                   |Meaning
----                   |-------
Driver                 |Process that contains the Spark Context
Executor               |Process that executes one or more Spark tasks
Master                 |Process which manages applications across the cluster
                       |E.g. Spark Master
Worker                 |Process which manages executors on a particular worker node
                       |E.g. Spark Worker

Spark Job
---------

Q: Flip a coin 100 times using Python's `random()` function. What
fraction of the time do you get heads?

- Initialize Spark.

        from pyspark import SparkContext
        sc = SparkContext()

- Import random.

        import random
        flips = 1000000
        heads = sc.parallelize(xrange(flips)) \
            .map(lambda i: random.random()) \
            .filter(lambda r: r < 0.51) \
            .count()

        ratio = float(heads)/float(flips)

        print(heads)
        print(ratio)

Notes
-----

- `sc.parallelize` creates an RDD.

- `map` and `filter` are *transformations*.

- They create new RDDs from existing RDDs.

- `count` is an *action* and brings the data from the RDDs back to the
  driver.

Spark Terminology
-----------------

Term                   |Meaning
----                   |-------
RDD                    |*Resilient Distributed Dataset* or a distributed sequence of records
Spark Job              |Sequence of transformations on data with a final action
Spark Application      |Sequence of Spark jobs and other code
Transformation         |Spark operation that produces an RDD
Action                 |Spark operation that produces a local object


- A Spark job consists of a series of transformations followed by an
  action.

- It pushes the data to the cluster, all computation happens on the
  *executors*, then the result is sent back to the driver.

Pop Quiz
--------

<details><summary>
In this Spark job what is the transformation is what is the action? 
`sc.parallelize(xrange(10)).filter(lambda x: x % 2 == 0).collect()`
</summary>
1. `filter` is the transformation.
<br>
2. `collect` is the action.
</details>

Lambda vs Functions
-------------------

- Instead of `lambda` you can pass in fully defined functions into
  `map`, `filter`, and other RDD transformations.

- Use `lambda` for short functions. 

- Use `def` for more substantial functions.

Finding Primes
--------------

Q: Find all the primes less than 100.

- Define function to determine if a number is prime.

        def is_prime(number):
            factor_min = 2
            factor_max = int(number**0.5)+1
            for factor in xrange(factor_min,factor_max):
                if number % factor == 0:
                    return False
            return True

- Use this to filter out non-primes.

        numbers = xrange(2,100)
        primes = sc.parallelize(numbers)\
            .filter(is_prime)\
            .collect()
        print primes

Pop Quiz
--------

<img src="images/spark-cluster.png">

<details><summary>
Q: Where does `is_prime` execute?
</summary>
On the executors.
</details>

<details><summary>
Q: Where does the RDD code execute?
</summary>
On the driver.
</details>

Transformations and Actions
===========================

Common RDD Constructors
-----------------------

Expression                               |Meaning
----------                               |-------
`sc.parallelize(list1)`                  |Create RDD of elements of list
`sc.textFile(path)`                      |Create RDD of lines from file

Common Transformations
----------------------

Expression                               |Meaning
----------                               |-------
`filter(lambda x: x % 2 == 0)`           |Discard non-even elements
`map(lambda x: x * 2)`                   |Multiply each RDD element by `2`
`map(lambda x: x.split())`               |Split each string into words
`flatMap(lambda x: x.split())`           |Split each string into words and flatten sequence
`sample(withReplacement=True,0.25)`      |Create sample of 25% of elements with replacement
`union(rdd)`                             |Append `rdd` to existing RDD
`distinct()`                             |Remove duplicates in RDD
`sortBy(lambda x: x, ascending=False)`   |Sort elements in descending order


Common Actions
--------------

Expression                             |Meaning
----------                             |-------
`collect()`                            |Convert RDD to in-memory list 
`take(3)`                              |First 3 elements of RDD 
`top(3)`                               |Top 3 elements of RDD
`takeSample(withReplacement=True,3)`   |Create sample of 3 elements with replacement
`sum()`                                |Find element sum (assumes numeric elements)
`mean()`                               |Find element mean (assumes numeric elements)
`stdev()`                              |Find element deviation (assumes numeric elements)

Pop Quiz
--------

Q: What will this output?

    sc.parallelize([1,3,2,2,1]).distinct().collect()

Q: What will this output?

    sc.parallelize([1,3,2,2,1]).sortBy(lambda x: x).collect()

Q: What will this output?

- Create this input file. 

        %%writefile input.txt
        hello world
        another line
        yet another line
        yet another another line

- What do you get when you run this code?

        sc.textFile('input.txt') \
            .map(lambda x: x.split()) \
            .count()

- What about this?

        sc.textFile('input.txt') \
            .flatMap(lambda x: x.split()) \
            .count()

Map vs FlatMap
--------------

- Here's the difference between `map` and `flatMap`.

- Map:

        sc.textFile('input.txt') \
            .map(lambda x: x.split()) \
            .collect()

- FlatMap:

        sc.textFile('input.txt') \
            .flatMap(lambda x: x.split()) \
            .collect()

Key Value Pairs
===============

PairRDD
-------

At this point we know how to aggregate values across an RDD. If we
have an RDD containing sales transactions we can find the total
revenue across all transactions.

Q: Using the following sales data find the total revenue across all
transactions.

    %%writefile sales.txt
    #ID    Date           Store   State  Product    Amount
    101    11/13/2014     100     WA     331        300.00
    104    11/18/2014     700     OR     329        450.00
    102    11/15/2014     203     CA     321        200.00
    106    11/19/2014     202     CA     331        330.00
    103    11/17/2014     101     WA     373        750.00
    105    11/19/2014     202     CA     321        200.00

- Read the file.

        sc.textFile('sales.txt')\
            .take(2)

- Split the lines.

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .take(2)

- Remove `#`.

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .filter(lambda x: x[0].startswith('#'))\
            .take(2)

- Try again.

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .filter(lambda x: not x[0].startswith('#'))\
            .take(2)

- Pick off last field. 

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .filter(lambda x: not x[0].startswith('#'))\
            .map(lambda x: x[-1])\
            .take(2)

- Convert to float and then sum.

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .filter(lambda x: not x[0].startswith('#'))\
            .map(lambda x: float(x[-1]))\
            .sum()

ReduceByKey
-----------

Q: Calculate revenue per state?

- Instead of creating a sequence of revenue numbers we can create
  tuples of states and revenue.

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .filter(lambda x: not x[0].startswith('#'))\
            .map(lambda x: (x[-3],float(x[-1])))\
            .collect()

- Now use `reduceByKey` to add them up.

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .filter(lambda x: not x[0].startswith('#'))\
            .map(lambda x: (x[-3],float(x[-1])))\
            .reduceByKey(lambda amount1,amount2: amount1+amount2)\
            .collect()

Q: Find the state with the highest total revenue.

- You can either use the action `top` or the transformation `sortBy`.

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .filter(lambda x: not x[0].startswith('#'))\
            .map(lambda x: (x[-3],float(x[-1])))\
            .reduceByKey(lambda amount1,amount2: amount1+amount2)\
            .sortBy(lambda state_amount:state_amount[1],ascending=False) \
            .collect()

Pop Quiz
--------

<details><summary>
Q: What does `reduceByKey` do?
</summary>
1. It is like a reducer.
<br>
2. If the RDD is made up of key-value pairs, it combines the values
   across all tuples with the same key by using the function we pass
   to it.
<br>
3. It only works on RDDs made up of key-value pairs or 2-tuples.
</details>

Notes
-----

- `reduceByKey` only works on RDDs made up of 2-tuples.

- `reduceByKey` works as both a reducer and a combiner.

- It requires that the operation is associative.

Word Count
----------

Q: Implement word count in Spark.

- Create some input.

        %%writefile input.txt
        hello world
        another line
        yet another line
        yet another another line

- Count the words.

        sc.textFile('input.txt')\
            .flatMap(lambda line: line.split())\
            .map(lambda word: (word,1))\
            .reduceByKey(lambda count1,count2: count1+count2)\
            .collect()

Making List Indexing Readable
-----------------------------

- While this code looks reasonable, the list indexes are cryptic and
  hard to read.

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .filter(lambda x: not x[0].startswith('#'))\
            .map(lambda x: (x[-3],float(x[-1])))\
            .reduceByKey(lambda amount1,amount2: amount1+amount2)\
            .sortBy(lambda state_amount:state_amount[1],ascending=False) \
            .collect()

- We can make this more readable using Python's argument unpacking
  feature.

Argument Unpacking
------------------

Q: Which version of `getCity` is more readable and why?

- Consider this code.

        client = ('Dmitri','Smith','SF')

        def getCity1(client):
            return client[2]

        def getCity2((first,last,city)):
            return city

        print getCity1(client)

        print getCity2(client)

- What is the difference between `getCity1` and `getCity2`?

- Which is more readable?

- What is the essence of argument unpacking?

Pop Quiz
--------
<details><summary>
Q: Can argument unpacking work for deeper nested structures?
</summary>
Yes. It can work for arbitrarily nested tuples and lists.
</details>

<details><summary>
Q: How would you write `getCity` given 
`client = ('Dmitri','Smith',('123 Eddy','SF','CA'))`
</summary>
`def getCity((first,last,(street,city,state))): return city`
</details>

Argument Unpacking
------------------

- Lets test this out.

        client = ('Dmitri','Smith',('123 Eddy','SF','CA'))

        def getCity((first,last,(street,city,state))):
            return city

        getCity(client)

- Whenever you find yourself indexing into a tuple consider using
  argument unpacking to make it more readable.

- Here is what `getCity` looks like with tuple indexing.

        def badGetCity(client):
            return client[2][1]

        getCity(client)

Argument Unpacking In Spark
---------------------------

Q: Rewrite the last Spark job using argument unpacking.

- Here is the original version of the code.

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .filter(lambda x: not x[0].startswith('#'))\
            .map(lambda x: (x[-3],float(x[-1])))\
            .reduceByKey(lambda amount1,amount2: amount1+amount2)\
            .sortBy(lambda state_amount:state_amount[1],ascending=False) \
            .collect()

- Here is the code with argument unpacking.

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .filter(lambda x: not x[0].startswith('#'))\
            .map(lambda (id,date,store,state,product,amount): (state,float(amount)))\
            .reduceByKey(lambda amount1,amount2: amount1+amount2)\
            .sortBy(lambda (state,amount):amount,ascending=False) \
            .collect()

- In this case because we have a long list or tuple argument unpacking
  is a judgement call.

GroupByKey
----------

`reduceByKey` lets us aggregate values using sum, max, min, and other
associative operations. But what about non-associative operations like
average? How can we calculate them?

- There are several ways to do this.

- The first approach is to change the RDD tuples so that the operation
  becomes associative. 

- Instead of `(state, amount)` use `(state, (amount, count))`.

- The second approach is to use `groupByKey`, which is like
  `reduceByKey` except it gathers together all the values in an
  iterator. 
  
- The iterator can then be reduced in a `map` step immediately after
  the `groupByKey`.

Q: Calculate the average sales per state.

- Approach 1: Restructure the tuples.

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .filter(lambda x: not x[0].startswith('#'))\
            .map(lambda x: (x[-3],(float(x[-1]),1)))\
            .reduceByKey(lambda (amount1,count1),(amount2,count2): \
                (amount1+amount2, count1+count2))\
            .collect()

- Note the argument unpacking we are doing in `reduceByKey` to name
  the elements of the tuples.

- Approach 2: Use `groupByKey`.

        def mean(iter):
            total = 0.0; count = 0
            for x in iter:
                total += x; count += 1
            return total/count

        sc.textFile('sales.txt')\
            .map(lambda x: x.split())\
            .filter(lambda x: not x[0].startswith('#'))\
            .map(lambda x: (x[-3],float(x[-1])))\
            .groupByKey() \
            .map(lambda (state,iter): mean(iter))\
            .collect()

- Note that we are using unpacking again.

Pop Quiz
--------

<details><summary>
Q: What would be the disadvantage of not using unpacking?
</summary>
1. We will need to drill down into the elements.
<br>
2. The code will be harder to read.
</details>

<details><summary>
Q: What are the pros and cons of `reduceByKey` vs `groupByKey`?
</summary>
1. `groupByKey` stores the values for particular key as an iterable.
<br>
2. This will take up space in memory or on disk.
<br>
3. `reduceByKey` therefore is more scalable.
<br>
4. However, `groupByKey` does not require associative reducer
   operation.
<br>
5. For this reason `groupByKey` can be easier to program with.
</details>


Joins
-----

Q: Given a table of employees and locations find the cities that the
employees live in.


- The easiest way to do this is with a `join`.

        # Employees: emp_id, loc_id, name
        employee_data = [
            (101, 14, 'Alice'),
            (102, 15, 'Bob'),
            (103, 14, 'Chad'),
            (104, 15, 'Jen'),
            (105, 13, 'Dee') ]

        # Locations: loc_id, location
        location_data = [
            (14, 'SF'),
            (15, 'Seattle'),
            (16, 'Portland')]

        employees = sc.parallelize(employee_data)
        locations = sc.parallelize(location_data)

        # Re-key employee records with loc_id
        employees2 = employees.map(lambda (emp_id,loc_id,name):(loc_id,name));

        # Now join.
        employees2.join(locations).collect()

Pop Quiz
--------

<details><summary>
Q: How can we keep employees that don't have a valid location ID in
the final result?
</summary>
1. Use `leftOuterJoin` to keep employees without location IDs.
<br>
2. Use `rightOuterJoin` to keep locations without employees. 
<br>
3. Use `fullOuterJoin` to keep both.
<br>
</details>

RDD Details
===========

RDD Statistics
--------------

Q: How would you calculate the mean, variance, and standard deviation of a sample
produced by Python's `random()` function?

- Create an RDD and apply the statistical actions to it.

        count = 1000
        list = [random.random() for _ in xrange(count)]
        rdd = sc.parallelize(list)
        print rdd.mean()
        print rdd.variance()
        print rdd.stdev()

Pop Quiz
--------

<details><summary>
Q: What requirement does an RDD have to satisfy before you can apply
these statistical actions to it? 
</summary>
The RDD must consist of numeric elements.
</details>

<details><summary>
Q: What is the advantage of using Spark vs Numpy to calculate mean or standard deviation?
</summary>
The calculation is distributed across different machines and will be
more scalable.
</details>

RDD Laziness
------------

- Q: What is this Spark job doing?

        max = 10000000
        %time sc.parallelize(xrange(max)).map(lambda x:x+1).count()

- Q: How is the following job different from the previous one? How
  long do you expect it to take?

        %time sc.parallelize(xrange(max)).map(lambda x:x+1)

Pop Quiz
--------

<details><summary>
Q: Why did the second job complete so much faster?
</summary>
1. Because Spark is lazy. 
<br>
2. Transformations produce new RDDs and do no operations on the data.
<br>
3. Nothing happens until an action is applied to an RDD.
<br>
4. An RDD is the *recipe* for a transformation, rather than the
   *result* of the transformation.
</details>

<details><summary>
Q: What is the benefit of keeping the recipe instead of the result of
the action?
</summary>
1. It save memory.
<br>
2. It produces *resilience*. 
<br>
3. If an RDD loses data on a machine, it always knows how to recompute it.
</details>

Writing Data
------------

Besides reading data Spark and also write data out to a file system.

Q: Calculate the squares of integers from 1 to 100 and write them out
to `squares.txt`.

- Make sure `squares.txt` does not exist.

        !if [ -e squares.txt ] ; then rm -rf squares.txt ; fi

- Create the RDD and then save it to `squares.txt`.

        rdd1 = sc.parallelize(xrange(10))
        rdd2 = rdd1.map(lambda x: x*x)
        rdd2.saveAsTextFile('squares.txt')

- Now look at the output.

        !cat squares.txt

- Looks like the output is a directory.

        !ls -l squares.txt

- Lets take a look at the files.

        !for i in squares.txt/part-*; do echo $i; cat $i; done

Pop Quiz
--------

<details><summary>
Q: What's going on? Why are there two files in the output directory?
</summary>
1. There were two threads that were processing the RDD.
<br>
2. The RDD was split up in two partitions (by default).
<br>
3. Each partition was processed in a different task.
</details>

Partitions
----------

Q: Can we control the number of partitions/tasks that Spark uses for
processing data? Solve the same problem as above but this time with 5
tasks.

- Make sure `squares.txt` does not exist.

        !if [ -e squares.txt ] ; then rm -rf squares.txt ; fi

- Create the RDD and then save it to `squares.txt`.

        partitions = 5
        rdd1 = sc.parallelize(xrange(10), partitions)
        rdd2 = rdd1.map(lambda x: x*x)
        rdd2.saveAsTextFile('squares.txt')

- Now look at the output.

        !ls -l squares.txt
        !for i in squares.txt/part-*; do echo $i; cat $i; done

Pop Quiz
--------

<details><summary>
Q: How many partitions does Spark use by default?
</summary>
1. By default Spark uses 2 partitions.
<br>
2. If you read an HDFS file into an RDD Spark uses one partition per
   block.
<br>
3. If you read a file into an RDD from S3 or some other source Spark
   uses 1 partition per 32 MB of data.
</details>

<details><summary>
Q: If I read a file that is 200 MB into an RDD, how many partitions will that have?
</summary>
1. If the file is on HDFS that will produce 2 partitions (each is 128
   MB).
<br>
2. If the file is on S3 or some other file system it will produce 7
   partitions.
<br>
3. You can also control the number of partitions by passing in an
   additional argument into `textFile`.
</details>

Spark Terminology
-----------------

<img src="images/spark-cluster.png">

Term                   |Meaning
----                   |-------
Task                   |Single thread in an executor
Partition              |Data processed by a single task
Record                 |Records make up a partition that is processed by a single task

Notes
-----

- Every Spark application gets executors when you create a new `SparkContext`.

- You can specify how many cores to assign to each executor.

- A core is equivalent to a thread.

- The number of cores determine how many tasks can run concurrently on
  an executor.

- Each task corresponds to one partition.

Pop Quiz
--------

<details><summary>
Q: Suppose you have 2 executors, each with 2 cores--so a total of 4
cores. And you start a Spark job with 8 partitions. How many tasks
will run concurrently?
</summary>
4 tasks will execute concurrently.
</details>

<details><summary>
Q: What happens to the other partitions?
</summary>
1. The other partitions wait in queue until a task thread becomes
available.
<br>
2. Think of cores as turnstile gates at a train station, and
   partitions as people .
<br>
3. The number of turnstiles determine how many people can get through
   at once.
</details>

<details><summary>
Q: How many Spark jobs can you have in a Spark application?
</summary>
As many as you want.
</details>

<details><summary>
Q: How many Spark applications and Spark jobs are in this IPython Notebook?
</summary>
1. There is one Spark application because there is one `SparkContext`.
<br>
2. There are as many Spark jobs as we have invoked actions on RDDs.
</details>

Stock Quotes
------------

Q: Find the date on which AAPL's stock price was the highest.

Suppose you have stock market data from Yahoo! for AAPL from
<http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices>. The data is
in CSV format and has these values.

Date        |Open    |High    |Low     |Close   |Volume      |Adj Close
----        |----    |----    |---     |-----   |------      |---------
11-18-2014  |113.94  |115.69  |113.89  |115.47  |44,200,300  |115.47
11-17-2014  |114.27  |117.28  |113.30  |113.99  |46,746,700  |113.99

Here is what the CSV looks like:
    
    csv = [
      "#Date,Open,High,Low,Close,Volume,Adj Close\n",
      "2014-11-18,113.94,115.69,113.89,115.47,44200300,115.47\n",
      "2014-11-17,114.27,117.28,113.30,113.99,46746700,113.99\n",
    ]

Lets find the date on which the price was the highest. 


<details><summary>
Q: What two fields do we need to extract? 
</summary>
1. *Date* and *Adj Close*.
<br>
2. We want to use *Adj Close* instead of *High* so our calculation is
   not affected by stock splits.
</details>

<details><summary>
Q: What field should we sort on?
</summary>
*Adj Close*
</details>

<details><summary>
Q: What sequence of operations would we need to perform?
</summary>
1. Use `filter` to remove the header line.
<br>
2. Use `map` to split each row into fields.
<br>
3. Use `map` to extract *Adj Close* and *Date*.
<br>
4. Use `sortBy` to sort descending on *Adj Close*.
<br>
5. Use `take(1)` to get the highest value.
</details>

- Here is full source.

        csv = [
          "#Date,Open,High,Low,Close,Volume,Adj Close\n",
          "2014-11-18,113.94,115.69,113.89,115.47,44200300,115.47\n",
          "2014-11-17,114.27,117.28,113.30,113.99,46746700,113.99\n",
        ]
        sc.parallelize(csv) \
          .filter(lambda line: not line.startswith("#")) \
          .map(lambda line: line.split(",")) \
          .map(lambda fields: (float(fields[-1]),fields[0])) \
          .sortBy(lambda (close, date): close, ascending=False) \
          .take(1)

- Here is the program for finding the high of any stock that stores
  the data in memory.

        import urllib2
        import re

        def get_stock_high(symbol):
          url = 'http://real-chart.finance.yahoo.com' + \
            '/table.csv?s='+symbol+'&g=d&ignore=.csv'
          csv = urllib2.urlopen(url).read()
          csv_lines = csv.split('\n')
          stock_rdd = sc.parallelize(csv_lines) \
            .filter(lambda line: re.match(r'\d', line)) \
            .map(lambda line: line.split(",")) \
            .map(lambda fields: (float(fields[-1]),fields[0])) \
            .sortBy(lambda (close, date): close, ascending=False)
          return stock_rdd.take(1)

        get_stock_high('AAPL')


Notes
-----

- Spark is high-level like Hive and Pig.

- At the same time it does not invent a new language.

- This allows it to leverage the ecosystem of tools that Python,
  Scala, and Java provide.



Caching and Persistence
=======================

RDD Caching
-----------

- Consider this Spark job.

        import random
        num_count = 500*1000
        num_list = [random.random() for i in xrange(num_count)]
        rdd1 = sc.parallelize(num_list)
        rdd2 = rdd1.sortBy(lambda num: num)

- Lets time running `count()` on `rdd2`.

        %time rdd2.count()
        %time rdd2.count()
        %time rdd2.count()

- The RDD does no work until an action is called. And then when an
  action is called it figures out the answer and then throws away all
  the data.

- If you have an RDD that you are going to reuse in your computation
  you can use `cache()` to make Spark cache the RDD.

- Lets cache it and try again.

        rdd2.cache()
        %time rdd2.count()
        %time rdd2.count()
        %time rdd2.count()

- Caching the RDD speeds up the job because the RDD does not have to
  be computed from scratch again.

Notes
-----

- Calling `cache()` flips a flag on the RDD. 

- The data is not cached until an action is called.

- You can uncache an RDD using `unpersist()`.

Pop Quiz
--------

<details><summary>
Q: Will `unpersist` uncache the RDD immediately or does it wait for an
action?
</summary>
It unpersists immediately.
</details>

Caching and Persistence
-----------------------

Q: Persist RDD to disk instead of caching it in memory.

- You can cache RDDs at different levels.

- Here is an example.

        import pyspark
        rdd = sc.parallelize(xrange(100))
        rdd.persist(pyspark.StorageLevel.DISK_ONLY)

Pop Quiz
--------

<details><summary>
Q: Will the RDD be stored on disk at this point?
</summary>
No. It will get stored after we call an action.
</details>

Persistence Levels
------------------

Level                      |Meaning
-----                      |-------
`MEMORY_ONLY`              |Same as `cache()`
`MEMORY_AND_DISK`          |Cache in memory then overflow to disk
`MEMORY_AND_DISK_SER`      |Like above; in cache keep objects serialized instead of live 
`DISK_ONLY`                |Cache to disk not to memory

Notes
-----

- `MEMORY_AND_DISK_SER` is a good compromise between the levels. 

- Fast, but not too expensive.

- Make sure you unpersist when you don't need the RDD any more.


Spark Performance
=================

Narrow and Wide Transformations
-------------------------------

- Spark transformations are *narrow* if each RDD has one unique child
  past the transformation.

- Spark transformations are *wide* if each RDD can have multiple
  children past the transformation.

- Narrow transformations are map-like, while wide transformations are
  reduce-like.

- Narrow transformations are faster because they do move data between
  executors, while wide transformations are slower.
 
Repartitioning
--------------

- Over time partitions can get skewed. 

- Or you might have less data or more data than you started with.

- You can rebalance your partitions using `repartition` or `coalesce`.

- `coalesce` is narrow while `repartition` is wide.

Pop Quiz
--------

<details><summary>
Between `coalesce` and `repartition` which one is faster? Which one is
more effective?
</summary>
1. `coalesce` is narrow so it is faster. 
<br>
2. However, it only combines partitions and does not shuffle them.
<br>
3. `repartition` is wide but it partitions more effectively because it
   reshuffles the records.
</details>

Misc
====

Amazon S3
---------

- *"s3:" URLs break when Secret Key contains a slash, even if encoded*
    <https://issues.apache.org/jira/browse/HADOOP-3733>

- *Spark 1.3.1 / Hadoop 2.6 prebuilt pacakge has broken S3 filesystem access*
    <https://issues.apache.org/jira/browse/SPARK-7442>

<!--

Broadcast Variables

Accumulators

Checkpoint

S3 key issue

2.6

-->


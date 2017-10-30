{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Spark-ML\n",
    "\n",
    "Machine learning at a scale!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "# Objectives\n",
    "\n",
    "At the end of this lecture you should be able to:\n",
    "\n",
    "1. Chain spark dataframe methods together to do data munging.\n",
    "2. Be able to describe the Spark-ML API, and recognize differences to sk-learn.\n",
    "3. Chain Spark-ML Transformers and Estimators together to compose ML pipelines."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true,
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [],
   "source": [
    "import pyspark.sql.functions as F\n",
    "import sys\n",
    "sys.tracebacklimit = 0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Working with Spark DataFrames\n",
    "<br>\n",
    "\n",
    "## Examples to many similarites with Pandas"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Computing sales per state"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+---+----------+-----+-----+-------+------+\n",
      "|#ID|      Date|Store|State|Product|Amount|\n",
      "+---+----------+-----+-----+-------+------+\n",
      "|101|11/13/2014|  100|   WA|    331| 300.0|\n",
      "|104|11/18/2014|  700|   OR|    329| 450.0|\n",
      "|102|11/15/2014|  203|   CA|    321| 200.0|\n",
      "|106|11/19/2014|  202|   CA|    331| 330.0|\n",
      "|103|11/17/2014|  101|   WA|    373| 750.0|\n",
      "+---+----------+-----+-----+-------+------+\n",
      "only showing top 5 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Read CSV\n",
    "sales_df = sqlContext.read.csv('data/sales.csv',\n",
    "                               header=True,       # parse the first line as a header?\n",
    "                               quote='\"',         # quote character\n",
    "                               sep=\",\",           # separation character\n",
    "                               inferSchema=True)  # infer schema?\n",
    "\n",
    "sales_df.show(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### Pair Discussion - 2 mins\n",
    "\n",
    "You want to obtain a sorted DataFrame of the states in which you have the most sales (by amount).\n",
    "\n",
    "1. What transformations do you need to apply?\n",
    "2. How would you perform those transformations in Pandas?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+---+----------+-----+-----+-------+------+\n",
      "|#ID|      Date|Store|State|Product|Amount|\n",
      "+---+----------+-----+-----+-------+------+\n",
      "|101|11/13/2014|  100|   WA|    331| 300.0|\n",
      "+---+----------+-----+-----+-------+------+\n",
      "only showing top 1 row\n",
      "\n"
     ]
    }
   ],
   "source": [
    "sales_df.show(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "out_df = (sales_df.<insert_code_here>)\n",
    "\n",
    "out_df.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "slideshow": {
     "slide_type": "skip"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-----+------+\n",
      "|State| Money|\n",
      "+-----+------+\n",
      "|   WA|1050.0|\n",
      "|   CA| 730.0|\n",
      "|   OR| 450.0|\n",
      "+-----+------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Solution\n",
    "out_df = (sales_df.groupBy(sales_df.State)\n",
    "            # or           'State'\n",
    "                  .agg(F.sum(sales_df.Amount).alias('Money'))\n",
    "            # or       {'Amount': 'sum'} \n",
    "            # or  .sum('Amount')\n",
    "                  .orderBy('Money', ascending=False))\n",
    " \n",
    "out_df.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Find the date on which AAPL's closing stock price was the highest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+----------+----------+\n",
      "|                Date|      Open|      High|\n",
      "+--------------------+----------+----------+\n",
      "|2016-10-25 00:00:...|117.949997|118.360001|\n",
      "|2016-10-24 00:00:...|117.099998|117.739998|\n",
      "|2016-10-21 00:00:...|116.809998|116.910004|\n",
      "|2016-10-20 00:00:...|116.860001|117.379997|\n",
      "|2016-10-19 00:00:...|    117.25|117.760002|\n",
      "+--------------------+----------+----------+\n",
      "only showing top 5 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Read CSV\n",
    "aapl_df = sqlContext.read.csv('data/aapl.csv',\n",
    "                              header=True,       # parse the first line as a header?\n",
    "                              quote='\"',         # quote character\n",
    "                              sep=\",\",           # separation character\n",
    "                              inferSchema=True)  # infer schema?\n",
    "\n",
    "aapl_df.select('Date', 'Open', 'High').show(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### We can see the an intelligent schema has been inferred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "StructType(List(StructField(Date,TimestampType,true),StructField(Open,DoubleType,true),StructField(High,DoubleType,true),StructField(Low,DoubleType,true),StructField(Close,DoubleType,true),StructField(Volume,IntegerType,true),StructField(Adj Close,DoubleType,true)))"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(aapl_df.columns)\n",
    "aapl_df.schema"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### Pair Discussion - 2 Mins\n",
    "\n",
    "Now, design a pipeline that will:\n",
    "\n",
    "1. Keep only fields for `Date` and `Close`.\n",
    "2. Order by `Close` in descending order. How would you do this in Pandas?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+----------+----------+----------+------+--------+\n",
      "|                Date|      Open|      High|       Low| Close|  Volume|\n",
      "+--------------------+----------+----------+----------+------+--------+\n",
      "|2016-10-25 00:00:...|117.949997|118.360001|117.309998|118.25|39190300|\n",
      "+--------------------+----------+----------+----------+------+--------+\n",
      "only showing top 1 row\n",
      "\n"
     ]
    }
   ],
   "source": [
    "aapl_df.select('Date', 'Open', 'High', 'Low', 'Close', 'Volume').show(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "scrolled": true,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "out_df = aapl_df.(<insert_code_here>)\n",
    "\n",
    "out_df.show(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "skip"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+----------+\n",
      "|                Date|     Close|\n",
      "+--------------------+----------+\n",
      "|2015-11-03 00:00:...|    122.57|\n",
      "|2015-11-04 00:00:...|     122.0|\n",
      "|2015-11-02 00:00:...|    121.18|\n",
      "|2015-11-06 00:00:...|121.059998|\n",
      "|2015-11-05 00:00:...|120.919998|\n",
      "+--------------------+----------+\n",
      "only showing top 5 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Solution\n",
    "out_df = (aapl_df.select('Date', 'Close')\n",
    "                 .orderBy('Close', ascending=False))\n",
    "\n",
    "out_df.show(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Supervised Machine Learning on DataFrames\n",
    "\n",
    "http://spark.apache.org/docs/latest/ml-features.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']\n",
      "['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close', 'Features']\n",
      "+------------+\n",
      "|    Features|\n",
      "+------------+\n",
      "|    [118.25]|\n",
      "|[117.650002]|\n",
      "|[116.599998]|\n",
      "|[117.059998]|\n",
      "|[117.120003]|\n",
      "+------------+\n",
      "only showing top 5 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from pyspark.ml.feature import MinMaxScaler, VectorAssembler\n",
    "\n",
    "# Assemble values in a vector\n",
    "vectorAssembler = VectorAssembler(inputCols=[\"Close\"], \n",
    "                                  outputCol=\"Features\")\n",
    "\n",
    "vector_df = vectorAssembler.transform(aapl_df)\n",
    "print(aapl_df.columns)\n",
    "print(vector_df.columns)\n",
    "vector_df.select('Features').show(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Why does this difference matter?\n",
    "\n",
    "Let's try to run Spark-ML's built-in [min-max scaler](https://spark.apache.org/docs/latest/ml-features.html#minmaxscaler) the close column in our `appl_df`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "fail_scaler = MinMaxScaler(inputCol=\"Close\", outputCol=\"Scaled Close\")\n",
    "\n",
    "fail_scaler_model = fail_scaler.fit(aapl_df)\n",
    "\n",
    "scaled_close = fail_scaler_model.transform(aapl_df)\n",
    "scaled_close.show(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "### Gotta have the column be a vector..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------------+--------------------+\n",
      "|    Features|     Scaled Features|\n",
      "+------------+--------------------+\n",
      "|    [118.25]| [0.865963404782699]|\n",
      "|[117.650002]|[0.8473472730564975]|\n",
      "|[116.599998]|[0.8147688098332226]|\n",
      "|[117.059998]|[0.8290412250646944]|\n",
      "|[117.120003]|[0.8309029995776607]|\n",
      "+------------+--------------------+\n",
      "only showing top 5 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "scaler = MinMaxScaler(inputCol=\"Features\", outputCol=\"Scaled Features\")\n",
    "\n",
    "# Compute summary statistics and generate MinMaxScalerModel\n",
    "scaler_model = scaler.fit(vector_df)\n",
    "# Notice how we didn't specify the column, we already did above\n",
    "\n",
    "# Rescale each feature to range [min, max], returns a dataframe\n",
    "scaled_data = scaler_model.transform(vector_df)\n",
    "scaled_data.select(\"Features\", \"Scaled Features\").show(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Transformers and Estimators"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "# Transformers\n",
    "\n",
    "The `VectorAssembler` class above is an example of a generic type in Spark, called a [Transformer](http://spark.apache.org/docs/latest/ml-pipeline.html#transformers). Important things to know about this type:\n",
    "\n",
    "* They implement a `transform` method.\n",
    "* They convert one `DataFrame` into another, usually by adding columns.\n",
    "\n",
    "Examples of Transformers: [`VectorAssembler`](http://spark.apache.org/docs/latest/ml-features.html#vectorassembler), [`Tokenizer`](http://spark.apache.org/docs/latest/ml-features.html#tokenizer), [`StopWordsRemover`](http://spark.apache.org/docs/latest/ml-features.html#stopwordsremover), and [many more](http://spark.apache.org/docs/latest/ml-features.html).\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "# Estimators\n",
    "\n",
    "According to the docs: \"An [Estimator](http://spark.apache.org/docs/latest/ml-pipeline.html#estimators) abstracts the concept of a learning algorithm or any algorithm that fits or trains on data\". Important things to know about this type:\n",
    "\n",
    "* They implement a `fit` method whose argument is a `DataFrame`.\n",
    "* The output of `fit` is another type called `Model`, which is a `Transformer`.\n",
    "\n",
    "Examples of Estimators: [`LogisticRegression`](http://spark.apache.org/docs/latest/ml-classification-regression.html#logistic-regression), [`DecisionTreeRegressor`](http://spark.apache.org/docs/latest/ml-classification-regression.html#decision-tree-regression), and [many more](http://spark.apache.org/docs/latest/ml-classification-regression.html).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true,
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.ml import Pipeline\n",
    "from pyspark.ml.classification import LogisticRegression\n",
    "from pyspark.ml.feature import RegexTokenizer, HashingTF\n",
    "\n",
    "# Prepare training documents from a list of (id, text, label (about big data?)) tuples.\n",
    "train_df = spark.createDataFrame([\n",
    "             (0, \"spark is like hadoop mapreduce\", 1.0),\n",
    "             (1, \"sparks light fire!!!\", 0.0),\n",
    "             (2, \"elephants like simba\", 0.0),\n",
    "             (3, \"hadoop is an elephant\", 1.0),\n",
    "             (4, \"hadoop mapreduce\", 1.0)], \n",
    "             [\"id\", \"text\", \"label\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "regexTokenizer = RegexTokenizer(inputCol=\"text\", outputCol=\"tokens\", pattern=\"\\\\W\") # Transformer\n",
    "hashingTF = HashingTF(inputCol=\"tokens\", outputCol=\"features\") # Transformer\n",
    "lr = LogisticRegression(maxIter=10, regParam=0.001) # Estimator\n",
    "\n",
    "tokens_df = regexTokenizer.transform(train_df)\n",
    "hashes_df = hashingTF.transform(tokens_df)\n",
    "logistic_model = lr.fit(hashes_df) # Uses columns named features/label by default\n",
    "# logistic_model is now a transformer"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "### Now we can predict on new text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true,
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [],
   "source": [
    "# Prepare test documents, which are unlabeled (id, text) tuples.\n",
    "test_df = spark.createDataFrame([\n",
    "            (5, \"simba has a spark\"),\n",
    "            (6, \"hadoop\"),\n",
    "            (7, \"mapreduce in spark\"),\n",
    "            (8, \"apache hadoop\")], \n",
    "            [\"id\", \"text\"])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "### What do we need to do to this to get a prediction?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------------------+----------+--------------------+\n",
      "|              text|prediction|         probability|\n",
      "+------------------+----------+--------------------+\n",
      "| simba has a spark|       0.0|[0.78779795057740...|\n",
      "|            hadoop|       1.0|[0.02996000405249...|\n",
      "|mapreduce in spark|       1.0|[0.02396543994089...|\n",
      "|     apache hadoop|       1.0|[0.02996000405249...|\n",
      "+------------------+----------+--------------------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "preds_df = logistic_model.transform(\n",
    "                hashingTF.transform(\n",
    "           regexTokenizer.transform(test_df)))\n",
    "\n",
    "preds_df.select('text', 'prediction', 'probability').show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Pipelines\n",
    "\n",
    "Many data science workflows can be described as sequential application of various `Transforms` and `Estimators`. In `sklearn` we know that this idea has been formalized into a class, [`Pipeline`](http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html).\n",
    "\n",
    "This way of thinking about things was so popular that Spark decided to implement it exactly."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "![http://spark.apache.org/docs/latest/img/ml-Pipeline.png](http://spark.apache.org/docs/latest/img/ml-Pipeline.png)\n",
    "\n",
    "Let's see two ways to implement the above flow!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "## Configure an ML pipeline, which consists of three stages:\n",
    "* tokenizer,\n",
    "* hashingTF, and\n",
    "* logistic regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "regexTokenizer = RegexTokenizer(inputCol=\"text\", outputCol=\"tokens\", pattern=\"\\\\W\")\n",
    "hashingTF = HashingTF(inputCol=\"tokens\", outputCol=\"features\")\n",
    "lr = LogisticRegression(maxIter=10, regParam=0.001)\n",
    "pipeline = Pipeline(stages=[regexTokenizer, hashingTF, lr])\n",
    "\n",
    "# Fit the pipeline to training documents\n",
    "model = pipeline.fit(train_df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### And now `model` is a transformer representing the entire pipeline. So it's simple to run our `test_df` through."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------------------+----------+--------------------+\n",
      "|              text|prediction|         probability|\n",
      "+------------------+----------+--------------------+\n",
      "| simba has a spark|       0.0|[0.78779795057740...|\n",
      "|            hadoop|       1.0|[0.02996000405249...|\n",
      "|mapreduce in spark|       1.0|[0.02396543994089...|\n",
      "|     apache hadoop|       1.0|[0.02996000405249...|\n",
      "+------------------+----------+--------------------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "prediction = model.transform(test_df)\n",
    "prediction.select(['text', 'prediction', 'probability']).show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Unsupervised Machine Learning on DataFrames\n",
    "\n",
    "We can similarly do unsupervised learning in Spark ML. And we can still use pipelines!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-----------------+----------------+-----------------+----------------+\n",
      "|sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|\n",
      "+-----------------+----------------+-----------------+----------------+\n",
      "|              5.1|             3.5|              1.4|             0.2|\n",
      "|              4.9|             3.0|              1.4|             0.2|\n",
      "|              4.7|             3.2|              1.3|             0.2|\n",
      "|              4.6|             3.1|              1.5|             0.2|\n",
      "|              5.0|             3.6|              1.4|             0.2|\n",
      "+-----------------+----------------+-----------------+----------------+\n",
      "only showing top 5 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Read CSV\n",
    "iris_df = sqlContext.read.csv('data/iris.csv',\n",
    "                              header=True,       # parse the first line as a header?\n",
    "                              quote='\"',         # quote character\n",
    "                              sep=\",\",           # separation character\n",
    "                              inferSchema=True)  # infer schema?\n",
    "\n",
    "iris_df.show(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+\n",
      "|         pcaFeatures|\n",
      "+--------------------+\n",
      "|[-2.8271359726790...|\n",
      "|[-2.7959524821488...|\n",
      "|[-2.6215235581650...|\n",
      "|[-2.7649059004742...|\n",
      "|[-2.7827501159516...|\n",
      "+--------------------+\n",
      "only showing top 5 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from pyspark.ml.feature import PCA\n",
    "\n",
    "col_names = [\"sepal length (cm)\", \"sepal width (cm)\", \n",
    "             \"petal length (cm)\", \"petal width (cm)\"]\n",
    "pcaVectorAssembler = VectorAssembler(inputCols=col_names, outputCol=\"features\")\n",
    "pca = PCA(k=3, inputCol=\"features\", outputCol=\"pcaFeatures\")\n",
    "pipeline = Pipeline(stages=[pcaVectorAssembler, pca])\n",
    "\n",
    "fitted_pipeline = pipeline.fit(iris_df)\n",
    "\n",
    "fitted_pipeline.transform(iris_df).select(\"pcaFeatures\").show(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Inspecting Pipelines\n",
    "\n",
    "We can even access the individual, fitted, parts of a pipeline if there's an attribute on them that we're in"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DenseVector([0.9246, 0.053, 0.0172])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fitted_pipeline.stages[-1].explainedVariance"
   ]
  }
 ],
 "metadata": {
  "celltoolbar": "Slideshow",
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}

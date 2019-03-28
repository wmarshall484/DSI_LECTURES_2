# Part 2: Machine Learning on Your Cluster

Here we will use the K-Means algorithm to build a model that would cluster Wikipedia articles and be able to predict the topic of a new article.

Make sure that you've set up an EMR cluster with the `launch_cluster.sh` script, and you can access a Jupyter notebook running on the master node.

### Distributed Machine Learning

**WARNING: To avoid unnecessary AWS usage fees, be sure to terminate your clusters when you are done using them.**

1. Include the following libraries.

    ```python
    import numpy as np
    import string
    import re

    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer

    from pyspark.ml.clustering import KMeans
    from pyspark.ml.feature import CountVectorizer, IDF
    from pyspark.sql.functions import udf
    from pyspark.sql.types import ArrayType, StringType
    from pyspark.sql import Row

    PUNCTUATION = set(string.punctuation)
    STOPWORDS = set(stopwords.words('english'))
    ```

2. The bucket `s3a://galv-wiki-data/` contains a dump of the text of every wikipedia article. The directory `wiki_full` contains a bunch of folders. Each folder contains files, and each line of each file is a json string containing article text and some metadata. The directory `wiki_mini` contains a subsample of about 10% of the full dataset. Load the subset of articles into a dataframe with 

   `wiki_df = spark.read.json('s3a://galv-wiki-data/wiki_mini/*/')`
   
 then check out the schema and a few rows.
   
3. We can safely cache the whole data set into memory as we have plenty of memory at our disposal for a data set of this size.

   ```python
   wiki_df.cache() # same as persist()
   ```

4. Count the total number of documents.

5. For testing out our pipeline, let's make a smaller dataframe with ~1000 entries. Use `wiki_small = wiki_df.sample()` to accomplish this.

6. Tokenize and stem each of your articles in the DF. Use the tokenizer below as a starting point.

```python
def tokenize(text):
    regex = re.compile('<.+?>|[^a-zA-Z]')
    clean_txt = regex.sub(' ', text)
    tokens = clean_txt.split()
    lowercased = [t.lower() for t in tokens]

    no_punctuation = []
    for word in lowercased:
        punct_removed = ''.join([letter for letter in word if not letter in PUNCTUATION])
        no_punctuation.append(punct_removed)
    no_stopwords = [w for w in no_punctuation if not w in STOPWORDS]

    STEMMER = PorterStemmer()
    stemmed = [STEMMER.stem(w) for w in no_stopwords]
    return [w for w in stemmed if w]
```

7. The above `tokenize` function takes in a string and outputs a list of strings. To apply this to every string in a Spark Dataframe, you will need to use Spark's special [user-defined-function](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.functions.udf) wrapper. Note that you need to specify the type of the output of your function with the `returnType` keyword in `udf()`. Then use [`.withColumn()`](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame.withColumn) to make a new column called `tokens` using the udf. For example, 
```python
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType, FloatType, StringType, ArrayType

tokenize_udf = udf(tokenize, returnType=###SPECIFY RETURN TYPES HERE ###)

wiki_df_tokens = wiki_small.withColumn("tokens", tokenize_udf(wiki_small['text']))
```

Note further that when specifying `ArrayType()`, you need to specify the type of data in the array (for example, `[4,3,1]` would be `ArrayType(IntegerType())`).

8. Compute term frequency for each document using the [`CountVectorizer`](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#pyspark.ml.feature.CountVectorizer) function in the [`pyspark.ml`](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#pyspark-ml-package) library. A couple of things to keep in mind:
    * We suggest you limit the vocabulary size to 5000 and set the minimum document frequency to 10.
    * You'll need to use the `.fit()` method of the CountVectorizer object and the `.transform()` method of the model object returned by `.fit()`.
    * You can see the terms that your CountVectorizer model knows about in its `.vocabulary` attribute.

9. Using the term frequency column you just created compute inverse document frequency for each document using the [`IDF`](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#pyspark.ml.feature.IDF) function in the [`pyspark.ml`](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#pyspark-ml-package) library. A couple of tips:
    * As with the CountVectorizer you will have to use the `.fit()` and `.transform()` methods.
    * We are going to be using the output of this model to do our KMeans clustering. The KMeans model, by default, takes a features columns named "features", so you can either name the output of this model "features" or you can name it something else and explicitly tell your KMeans model in the next step that name.
    * Despite its name, the `IDF` function actually returns the TF-IDF values that we're accustomed to. What the function actually does is scale a term frequency column by an IDF vector that it calculates, see [this](http://spark.apache.org/docs/latest/ml-features.html#tf-idf) guide for more discussion. This vector can be seen on the model's `idf` attribute.
    * If you cache this final DataFrame the following steps will run faster. Why do you think this is?

10. Make a [KMeans](http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#pyspark.ml.clustering.KMeans) object and train with the IDF column you just created. Start with a lower number of clusters (5). Fewer clusters will take less time to run.

11. Access the centroids with the `.clusterCenters()` method on your fitted KMeans model. Write a function to access the top `n` words with the highest TF-IDF in the each of the centroids. To do this you function will need:
    * The number of words to select.
    * The token for each of the dimensions of the centroids. (Hint: look at the vocabulary from the CountVectorizer).
    * The centroids from a trained KMeans model.

    **WARNING: To avoid unnecessary AWS usage fees, be sure to terminate your clusters when you are done using them.**

### Extra Credit

1. Write a file with the top words per centroid and transfer the files you have written to your bucket with `boto`. Refer to [this](https://github.com/gschool/dsi-high-performance-python/blob/master/individual.md) previous sprint for instructions.

2. Now you have tested your code on an example of 1000. You can run on the whole set and leave the IPython Notebook running. To do this consider the following steps:
    1. Stop the notebook, and restart it inside of a tmux session.
    2. Condense all of the steps you went through to fit your KMeans model on the sample of data into a function that accepts a DF with Wikipedia data in it.
    3. Run your function, passing it the DF with the full Wikipedia data set.

    If you start the notebook in tmux you can now detach from that session, log out of your instance and still track the progress of the jobs via the UI.

3. If you prefer not to run in an IPython notebook, consider putting your function into a script and [adding a step](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/add-steps-cli-console.html) to your cluster. If you do this you should plan on writing the output of your script, either a summary from the model or even a pickled version of it, to your bucket since you won't be able to do anything with it after the step completes.


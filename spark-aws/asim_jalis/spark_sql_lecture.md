
    %%javascript
    $.getScript('http://asimjalis.github.io/ipyn-ext/js/ipyn-present.js')

<img src="images/spark-logo.png">

<h1 class="tocheading">Spark SQL</h1>
<div id="toc"></div>

Spark SQL
=========

Spark SQL
---------

What is Spark SQL?

- Spark SQL takes basic RDDs and puts a schema on them.

What are schemas?

- Schema = Table Names + Column Names + Column Types

What are the pros of schemas?

- Schemas enable using column names instead of column positions

- Schemas enable queries using SQL and DataFrame syntax

- Schemas make your data more structured.

Pop Quiz
--------

<details><summary>
What are the cons of schemas?
</summary>
1. Schemas make your data more structured.
<br>
2. They make things more fragile.
<br>
3. Y2K was a schema-problem.
</details>


Start Spark SQL
---------------

How can I start using Spark SQL?

- Create a SparkContext.

        import pyspark
        sc = pyspark.SparkContext()
        print sc

- Create a HiveContext.

        sqlContext = pyspark.HiveContext(sc)
        print sqlContext

- Instead of a HiveContext you can initialize `sqlContext` using
  `pyspark.SqlContext(sc)`

- However, this is less preferred.

What is the difference between SparkContext and HiveContext?

- HiveContext gives you access to the metadata stored in Hive.

- This enables Spark SQL to interact with tables created in Hive.

- Hive tables can be backed by HDFS files, S3, HBase, and other data
  sources.

DataFrame, Schema, SchemaRDD
----------------------------

What is a DataFrame?

- DataFrames are the primary abstraction in Spark SQL.

- Think of a DataFrames as RDDs with schema. 

What is a schema?

- Schemas are metadata about your data.

- Schemas define table names, column names, and column types over your
  data.

- Schemas enable using SQL and DataFrame syntax to query your RDDs,
  instead of using column positions.

What is a SchemaRDD?

- Spark 1.3 introduced the concept of a DataFrame as the primary SQL
  abstraction.

- Before Spark 1.3 DataFrames were called SchemaRDD.

- Some of the DataFrame syntax will require using Spark 1.3 or later.

- Watch out for syntax changes.

- We will use the term DataFrame to refer to both SchemaRDDs and
  DataFrames.

Spark SQL Using CSV
-------------------

How can I pull in my CSV data and use Spark SQL on it?

- Make sure the CSV exists.

        %%writefile sales.csv
        #ID,Date,Store,State,Product,Amount
        101,11/13/2014,100,WA,331,300.00
        104,11/18/2014,700,OR,329,450.00
        102,11/15/2014,203,CA,321,200.00
        106,11/19/2014,202,CA,331,330.00
        103,11/17/2014,101,WA,373,750.00
        105,11/19/2014,202,CA,321,200.00

- Read the file and convert columns to right types.

        rdd = sc.textFile('sales.csv')\
            .filter(lambda line: not line.startswith('#'))\
            .map(lambda line: line.split(','))\
            .map(lambda \
              (id,date,store,state,product,amount):\
              (int(id),date,int(store),state,int(product),float(amount)))
        rdd.collect()

- Import data types.

        from pyspark.sql.types import *

- Define a schema.

        schema = StructType( [
            StructField('id',IntegerType(),True),
            StructField('date',StringType(),True),
            StructField('store',IntegerType(),True),
            StructField('state',StringType(),True),
            StructField('product',IntegerType(),True),
            StructField('amount',FloatType(),True) ] )

- Define the DataFrame object. Note: This will only work with Spark
  1.3 or later.

        df = sqlContext.createDataFrame(rdd,schema)
        df.show()

- If your version of Spark is earlier than 1.3 use the following
  syntax instead. 

        df = sqlContext.applySchema(rdd, schema)
        df.show()

- The older syntax will work in Spark 1.3 and later as well, but it
  will give you deprecation warnings.

Pop Quiz
--------

<details><summary>
What change do we have to make to the code above if we are
processing a TSV file instead of a CSV file?
</summary>
<br>
Replace `line.split(',')` with `line.split()`
</details>

Using SQL With DataFrames
-------------------------

How can I run SQL queries on DataFrames?

- Register the table with SqlContext.

        df.registerTempTable('sales')

- Run queries on the registered tables.

        result = sqlContext.sql(
            'SELECT state,amount from sales where amount > 100')

- View the results using `show()` or `collect()`.

        result.show()
        result.collect()

Pop Quiz
--------

<details><summary>
If I run `result.collect()` twice how many times will the data be read
from disk?
</summary>
1. RDDs are lazy.<br>
2. Therefore the data will be read twice.<br>
3. Unless you cache the RDD, All transformations in the RDD will
execute on each action.<br>
</details>

Caching Tables
--------------

How can I cache the RDD for a table to avoid roundtrips to disk on
each action?

- Use `cacheTable()`.

        sqlContext.cacheTable('sales');

- This is particularly useful if you are using Spark SQL to explore
  data.

Saving Results
--------------

How can I save the results back out to the file system?

- Make sure the files do not exist.

        !rm -rf high-sales.json high-sales.parquet

- You can either write them out using the JSON format.

        result.toJSON().saveAsTextFile('high-sales.json')

- Or you can save them as Parquet.

        result.write.parquet('high-sales.parquet')

- Lets take a look at the files.

        !ls -l sales.csv high-sales.json high-sales.parquet 
        !for i in high-sales.json/part-*; do echo $i; cat $i; done

Spark SQL Using JSON Data
-------------------------

What is JSON-formatted data?

- In Spark the JSON format means that each line is a JSON document.

- JSON-formatted data can be saved as text using `saveAsTextFile()` and
  read using `textFile()`.

- JSON works well with Spark SQL because the data has an embedded
  schema.

What other formats are supported by Spark SQL?

- Spark SQL also supports Parquet, which is a compact binary format
  for big data.

- If your data is in CSV then you have to add the schema
  programmatically after you load the data.

Parsing JSON Data
-----------------

How can I read JSON input and put it into a DataFrame?

- First make sure the file exists.

        %%writefile sales.json
        {"id":101, "date":"11/13/2014", "store":100, "state":"WA", "product":331, "amount":300.00}
        {"id":104, "date":"11/18/2014", "store":700, "state":"OR", "product":329, "amount":450.00}
        {"id":102, "date":"11/15/2014", "store":203, "state":"CA", "product":321, "amount":200.00}
        {"id":106, "date":"11/19/2014", "store":202, "state":"CA", "product":331, "amount":330.00}
        {"id":103, "date":"11/17/2014", "store":101, "state":"WA", "product":373, "amount":750.00}
        {"id":105, "date":"11/19/2014", "store":202, "state":"CA", "product":321, "amount":200.00}

- Now read in the file.

        sales = sqlContext.read.json('sales.json')

- JSON is self-describing and does not require defining a schema.

How can inspect my DataFrame?

- Use `show()` to look at the first 20 rows of the DataFrame.

        sales.show()

- Here is how to look at a 50% sample of the DataFrame (without
  replacement).

        sales.sample(False,0.5).show()

- Here is how to inspect the schema.

        print sales.schema
        print '--'
        print sales.schema.fields
        print '--'
        print sales.describe()
        print '--'
        sales.printSchema()

DataFrame Methods
-----------------

How can I slice the DataFrame by column and by row?

- DataFrames provide a *Pandas*-like API for manipulating data.

- To select specific columns use `select()`.

        sales.select('state','amount').show()

- You can also modify the columns while selecting.

        sales.select('state',sales.amount+100).show()
        sales.select('state',sales['amount']+100).show()

- You can evaluate boolean expressions.

        sales.select('state',sales.amount<300).show()
        sales.select('state',sales.amount == 300).show()

- You can group values.

        sales.select('state','amount').groupBy('state').count().show()

- You can filter rows based on conditions.

        sales.filter(sales.state == 'CA').show()

- You can use SQL to write more elaborate queries.

        sales.registerTempTable('sales')
        sqlContext.sql('select * from sales where amount > 300').show()

How can I convert DataFrames to regular RDDs?

- DataFrames are also RDDs.

- You can use `map()` to iterate over the rows of the DataFrame.

- You can access the values in a row using field names or column names.

        sales.map(lambda row: row.amount).collect()

- You can also use `collect()` or `take()` to pull DataFrame rows into
  the driver.

        sales.collect()

How can I convert Spark DataFrames to Pandas data frames?

- Use `toPandas()` to convert Spark DataFrames to Pandas.

        x = sales.toPandas()
        print type(x)
        print x

JSON vs CSV vs Parquet 
----------------------

What are the pros and cons of JSON vs CSV vs Parquet?

Feature            |JSON               |CSV            |Parquet
-------            |----               |---            |-------
Human-Readable     |Yes                |Yes            |No
Compact            |No                 |Moderately     |Highly
Columnar           |No                 |No             |Yes
Self-Describing    |Yes                |No             |Yes
Requires Schema    |No                 |Yes            |No
Splittable         |Yes                |Yes            |Yes
Popular            |No                 |Yes            |Not yet

What are columnar data formats?

- Columnar data formats store data column-wise.

- This allows them to do RLE or run-length encoding.

- Instead of storing `San Francisco` 100 times, they will just store
  it once and the count of how many times it occurs.

- When the data is repetitive and redundant as unstructured big data
  tends to be, columnar data formats use up a fraction of the disk
  space of non-columnar formats.

What are splittable data formats?

- On big data systems data is stored in blocks.

- For example, on HDFS data is stored in 128 MB blocks.

- Splittable data formats enable records in a block to be processed
  without looking at the entire file.

What are some examples of a non-splittable data format?

- Gzip

User Defined Functions
----------------------

How can I create my own User-Defined Functions?

- Import the types (e.g. StringType, IntegerType, FloatType) that we
  are returning.

        from pyspark.sql.types import *

- Create a UDF to calculate sales tax of 10% on the amount.

        def add_tax(amount):
            return amount * 1.10

        sqlContext.registerFunction("add_tax", add_tax, FloatType())

- Apply the function.

        sqlContext.sql("SELECT *, add_tax(amount) AS with_tax FROM sales").show()

- Optional last argument of `registerFunction` is function return
  type; default is `StringType`.

- UDFs can single or multiple arguments. 

SQL Types
---------

How can I find out all the types that are available for SQL schemas
and UDF?

- In the IPython REPL type `import pyspark.sql.types`. 

- Then type `pyspark.sql.types.[TAB]`

- Autocomplete will show you all the available types.

Types          |Meaning
-----          |-------
StringType     |String
IntegerType    |Int
FloatType      |Float



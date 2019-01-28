# Using MongoDB with Docker

To start a container running the mongodb server,
```
$ docker run --name mongoserver -p 27017:27017 -d mongo
```

To access the mongo terminal in the container,
```
$ docker exec -it mongoserver mongo
```

To load data into the database,
```
$ cd path/to/data_dump.json
$ docker cp data_dump.json mongoserver:/home/
$ docker exec -it mongoserver bash
# cd /home/
# mongoimport --db database_name --collection collection_name < data_dump.json
```

# Using the MongoDB terminal
| command | description | 
|:--|:--|
|`show dbs` | show databases|
|`use db_name` | connect to database `db_name`|
|`show collections` | show collections (tables) in the database|
|`db.collection_name.find()` | return all records in the collection |
|`db.collection_name.find().limit(5)`| return 5 records in the collection|
|`db.collection_name.findOne()` | return one record in the collection|
|`db.collection_name.find().count()` | return the count of all records|
|`db.collection_name.insert({field_name_1:'example_string', field_name_2:['ex_list_item1', 'ex_list_item2']})`|insert a record into the collection. Mongo will create an `_id` field if not provided.|


## Query Examples

Say we have a collection called `users`. Let's add a few records.
```
db.users.insert({ name: 'Jon', age: '45', friends: [ 'Henry', 'Ashley']})

db.users.insert({ name: 'Ashley', age: '37', friends: [ 'Jon', 'Henry']})

db.users.insert({ name: 'Frank', age: '17',
                  friends: [ 'Billy'], car : 'Civic'})

db.users.find()
```
- Note: The three documents that we inserted into the above database didn't all have the same fields.
- Note: Mongo creates an `_id` field for each document if one isn't provided.


Now let's query these records based on some criteria:
```
db.users.find({ name: 'Jon'})               // find by single field

db.users.find({ car: { $exists : true } })  // find by presence of field

db.users.find({ friends: 'Henry' })         // find by value in array

db.users.find({}, { name: true })   // field selection (only return name)
```
A quick way to figure out how to write a Mongo query is to think about how you would do it in SQL and check out a resource like this Mongo endorsed [conversion guide](https://docs.mongodb.com/manual/reference/sql-comparison/#create-and-alter), or use something like a [query translator](http://www.querymongo.com/).

## Updating
```
// replaces friends array
db.users.update({name: "Jon"}, { $set: {friends: ["Phil"]}})

// adds to friends array
db.users.update({name: "Jon"}, { $push: {friends: "Susie"}})   

// upsert
db.users.update({name: "Stevie"}, { $push: {friends: "Nicks"}}, true)

// multiple updates
db.users.update({}, { $set: { activated : false } }, false, true)
```
[Documentation on updating](https://docs.mongodb.com/manual/reference/method/db.collection.update/)

[Documentation on aggregation](https://docs.mongodb.com/manual/reference/sql-aggregation-comparison/)

# Using PyMongo

First, install the pymongo package
```
$ conda install pymongo
```

Then, in ipython,
```
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['database_name']
table = db['collection_name']
```
Now you can use python to insert, update, and query records

```
example_record = {'name':'moses', 'age':31, friends:['ted', 'gahl']}

table.insert_one(example_record)

table.update_one('name':'moses', '$set':{'age':32})

table.find() # returns a generator for all records

table.find({'age':30} # find all records with age = 30

table.count_documents({}) # return the count of all records in the collection

# to view all the collections in a database
db.collection_names()
```


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
|`db.collection_name.find().limit(5)| return 5 records in the collection|
|`db.collection_name.findOne()` | return one record in the collection|
|`db.collection_name.find().count()` | return the count of all records|
|`db.collection_name.insert({field_name_1:'example_string', field_name_2:['ex_list_item1', 'ex_list_item2']})|insert a record into the collection. Mongo will create an `_id` field if not provided.|

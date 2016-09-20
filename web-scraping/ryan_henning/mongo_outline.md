# SQL vs NoSQL

NoSQL is short for one of "not SQL", "non relational", or "not only SQL".

The main idea with NoSQL is that data is stored WITHOUT A SCHEMA!

Recall, in RDBMSs, the schema is king. You have to plan your schema from the beginning and stick to it. If you want to change the schema, you have to have a database migration plan. There's a lot of overhead.

But with a NoSQL database, there is no schema. Just store what you want, whatever you have, no problem.

That sounds great doesn't it? Well, maybe. There's some drawbacks which we'll talk about at the end.

# MongoDB

Launch `mongod`. Explain that it is a little server.

Run `mongo --help`. Explain that it is a client that connects to a `mongod` server. Note that the default will be that it connects to 'localhost'.

Open TWO `mongo` clients (in two separate terminals).  Note that they are connected to the same 'localhost' server.

`mongo` gives us a _shell_ where we can issue commands.

In one terminal:

  - `show dbs`. That shows the database names.
  - `use demo_db`. That binds to the 'demo_db' database, creating it if it doesn't exist.
  - `db`. That's a reference to the current database ('demo_db' on our case).
  - `db.users`. That references the 'users' collection inside the current database. A collection is sorta like a table in an RDBMS.
  - `db.users.find()`. Think of the find method as SELECT from RDBMS world. It's the closest thing we have, anyway. This prints nothing because our users collection is empty.
  - `db.users.insert({})`. Insert an empty "document" (sorta like a row in an RDBMS).
  - `db.users.find()`. You should see that empty document now!

Now switch to the other terminal with the other `mongo` client. Show that our db, collection, and document show up.

Now switch back to the first terminal:

  - create a new document with: `db.users.insert({ 'name': 'Ryan', 'age': 84, 'friends': ['Scott C', 'Scott G', 'Scott S'] })`

  - see how it looks with: `db.users.find()`

  - create a new document with: `db.users.insert({ 'name': 'Scott C', 'age': 12, 'friends': ['Ryan', 'Scott G', 'Scott S'] })`

  - create a new document with: `db.users.insert({ 'name': 'Scott G', 'friends': ['Scott C', 'Ryan', 'Scott S'] })`

  - create a new document with: `db.users.insert({ 'name': 'Scott S', 'friends': ['Scott C', 'Scott G', 'Ryan'], 'fav_color': 'green' })`

  - see how it looks with: `db.users.find()`

Note how we can stick whatever we want in here. Mongo doesn't care. Mongo will *never* care.

Let's actually query for stuff:

  - `db.users.find().count()`

  - `db.users.find({ 'name': 'Ryan' })`

  - `db.users.find({ 'name': /Scott/ })`

  - `db.users.findOne({ 'name': /Scott/ })`

  - `db.users.find({ 'name': /Scott/ }, { 'friends': 1 })`   <-- 'inclusion query'

  - `db.users.find({ 'name': /Scott/ }, { 'friends': 0 })`   <-- 'exclusion query'

  - `db.users.find({ 'age': {'$lt': 50} })`

  - `db.users.find({ 'age': {'$lt': 50, '$gt': 20} })`

  - `db.users.update({ 'name': /Scott/ }, {'$set': {'gender': 'male'} })`

  - `db.users.update({ 'name': /Scott/ }, {'$set': {'gender': 'male'} }).pretty()`

Btw, what is this weird syntax? It's JSON. JavaScript Object Notation. Think of it like a dictionary in Python -- in fact, when we start using Python to talk to mongo (coming up soon), we'll use dictionaries.

Let's use tab to make our lives easier. Let's see if we can figure out how to get the names of all our collections. Type `db.` and hit tab. Read these. Which do you think will give us the name of our collections?

Let's get some help. Let's see if we can figure out how to get the count of our result set. Run `db.users.help()`. Do you see how to limit our results? How many Scotts are there?

Again. How to limit our result set to 2 Scott documents.

Again. How to get the distinct names?

Again. How to sort?

As such, the mongo shell is a JS interpreter. That's cool I guess...

Now do it in Python! Start `ipython` and do this:

```python
from pymongo import MongoClient
mongo_client = MongoClient()
db = mongo_client.demo_db
coll = db.users

coll.find({ 'name': 'Ryan' })

import re
scott_re = re.compile('Scott')
coll.find({ 'name': scott_re })
```

Back to the mongo shell. Run `db.help()`. How can we drop our database?

# Drawbacks of NoSQL

In machine learning, you need a matrix! Going from _relation_ (in RDBMS-world) to _matrix_ (say, in numpy-world) is quite easy. Going from Mongo _collection_ to _matrix_, probably not easy.

Typically, NoSQL DBs don't offer as much ACID as RDBMSs.

Typically, NoSQL DBs (where there tends to be duplicate data) take more storage than RDBMSs (where you can normalize your data -- e.g. use primary and foreign keys to avoid duplicating data).

The fact that you tend to duplicate data in NoSQL DBs means that modifying data is hard because you have to be sure to modify it in all places!

Complicated queries will be slower in NoSQL DBs because of their lack of structure, the DB cannot optimize nearly as well as in the structured world of RDBMSs.

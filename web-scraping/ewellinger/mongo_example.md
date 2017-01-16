---
title: Mongo Example
date: \today
author: Erich Wellinger
geometry: margin=1.25in
header-includes:
    - \usepackage{minted}
    - \newminted{python}{linenos, frame=lines, framesep=8pt, bgcolor=shadecolor}
---

\begin{minted}[linenos]{js}
// Start the server
mongod

// Start a Mongo shell
mongo

// Show the existing databases
show dbs

// Create a new database called class_db
use class_db

// View all the existing collections (tables)
db.getCollectionNames()

// Create a collection (table) and insert records into them
db.teachers.insert({name: 'E-Rich', age: 25, facial_hair: 'clean'})
db.teachers.insert({name: 'Frank', age: 21, friends: ['Adam', 'Cully']})
db.teachers.insert({name: 'Neil', age: 55, friends: ['Barack Obama', 'Kanye']})

// We can then view the first document in our table like so...
db.teachers.findOne()
db.teachers.findOne().pretty()

// Or we can view all our documents at once...
db.teachers.find().pretty()

// Or maybe we want to return the first 2 documents
db.teachers.find().limit(2).pretty()

// Generally speaking we run a .find({}, {}) where the first set of brackets
// dictates which documents get returned (like a WHERE clause) and the second
// set of brackets dictates which fields should be returned
db.teachers.find({name: 'Neil'}).pretty()
db.teachers.find({name: 'Neil'}, {friends: true}).pretty()
// By default, the id is always returned but we can turn that off
db.teachers.find({name: 'Neil'}, {friends: 1, _id: false}).pretty()

// Return only the friends entry from each document
db.teachers.find({}, {friends: true})

// Return all of each document (minus _id) for every document that has a friends field
db.teachers.find({friends: {$exists: true}}, {_id: false}).pretty()

// Return all the teachers that are under 30
db.teachers.find({age: {$lte: 30}}).pretty()

// Let's add up the ages of Neil and Frank
db.teachers.aggregate([
    { $match: { name: {$in : ['Frank', 'Neil'] } } },
    { $group: { _id: "$name", something: { $sum: "$age" } } },
    { $sort: { something: 1 } }
])

// Let's update Neil's facial hair status
db.teachers.update({name: "Neil"}, {$set : {facial_hair: 'Jesus Beard'}},
                   {multi: true, upsert: true})

// Let's kick it Old-School and update Frank's name to reflect that
db.teachers.find({name: "Frank"}).
            forEach(function(doc) {
            {
                id = doc._id;
                new_name = doc.name.replace("Frank", "Frank-The-Tank");
                db.teachers.update({ _id: id },
                                   {$set: {name: new_name}})
            };
        });

// Drop a particular collection
db.teachers.drop()
\end{minted}

# conda install pymongo (mac), sudo apt-get install python-pymongo
import pymongo #python wrapper for mongo
from pymongo import ASCENDING, DESCENDING #for sorted indexing
import pprint as pp #for pretty printing

#let's do some stuff together on the web (server hosted by Dan)
mongodb_uri = 'mongodb://heroku_xpbxqq54:1atu2i1t9nvr5jrgs10n4p7rdi@ds149820.mlab.com:49820/heroku_xpbxqq54'#'your_mongodb_uri_here (or set to None for localhost)'

client = pymongo.MongoClient(mongodb_uri) # Create MongoClient instance
db = client[pymongo.uri_parser.parse_uri(mongodb_uri)['database']]

############
#### BELOW CODE TO WORK ON A LOCAL MONGO INSTANCE
#work along in your own database on your own computer
client = pymongo.MongoClient()## Create MongoClient instance running on localhost
db_name='test_db'
db = client[db_name] #specify the database you want to work with
########

#let's create a collection

###DONT RUN THE FOLLOWING###
## db.drop_collection('student_collection') #dont do this, this will delete entire collection
## db.drop_collection('ermine_student_collection') #dont do this, this will delete entire collection
## db.drop_collection('article_word_counts') #dont do this, this will delete entire collection
############################

print db.collection_names()
collection_name = 'ermine_student_collection' # Specify the collection name to work with

#create new collection
STUDENTS = db[collection_name] # Get a collection instance
print db.collection_names()
#still not there because collection will only be really written to DB once we insert something or create and index

#optional indexing:
STUDENTS.create_index([('student_id', ASCENDING)],unique=True)
print db.collection_names()
#now the collection is there!

# Now we have a collection instance, ready to play with...

print STUDENTS.find_one()
#returns nothing

#now let's add something
student={'name':'joe','student_id':123,'class':'DS','favorite food':'tiramisu'}
STUDENTS.insert_one(student)
print STUDENTS.find_one()

#try again:
STUDENTS.insert_one(student)
##duplicate key error (unique key ID!)

#try new ID but rest the same
student={'name':'joe','student_id':124,'class':'DS','favorite_food':'tiramisu'}
STUDENTS.insert_one(student)

student={'name':'joe','class':'DS','favorite_food':'tiramisu'}
STUDENTS.insert_one(student)

student={'name':'joe','student_id':'abc','class':'DS','favorite_food':'tiramisu'}
STUDENTS.insert_one(student)


#DONT DO THIS UNLESS YOU KNOW YOUR COLLECTION IS SMALL
all_students=list(STUDENTS.find())
pp.pprint(all_students)

#wait a second, once we called the field "favorite food" and once "favorite_food" and Mongo didn't care!!


#what if suddenly I want to change what a certain field looks like? Maybe I want favorite_food to be a dictionary or a list and not a string. no problem in mongoDB!

#insert list instead of string
student={'name':'michelle','student_id':125,'class':'DS','favorite_food':['tiramisu','bananas']}
STUDENTS.insert_one(student)

#insert dict instead of string
student={'name':'ken','student_id':126,'class':'DS','favorite_food':{'dessert':'tiramisu','drink':'coffee'}}
STUDENTS.insert_one(student)

#mongo don't care! :-)
all_students=list(STUDENTS.find())
pp.pprint(all_students)
#all have different fields and different data types as values!


#retrieving data:
student = STUDENTS.find_one()
pp.pprint(student)

#find by field
student = STUDENTS.find_one({'student_id':125})
pp.pprint(student)
#print student

student = STUDENTS.find_one({'name':'joe'})
pp.pprint(student)
#print student

#find all entries with a certain value
all_joes = STUDENTS.find({'name':'joe'})

for joe in all_joes:
    pp.pprint(joe)

#filter by two fields
all_joes = STUDENTS.find({'name':'joe','student_id':123})
for joe in all_joes:
    pp.pprint(joe)
#only one returned!

#lets do some updating to our DB

#works just like the query but adds what needs to be changed
print STUDENTS.find_one({'name':'michelle'})
print "updating..."
student = STUDENTS.update_one({'name':'michelle'},{'$set':{'favorite_food':'chocolate_cake'}})
pp.pprint(STUDENTS.find_one({'name':'michelle'}))
#we just changed Michelle's favorite food from a list to a string without a problem!

#let's delete some stuff !!CAREFUL!!
pp.pprint(STUDENTS.find_one({'name':'michelle'}))
print "deleting..."
STUDENTS.delete_one({'name':'michelle'})
pp.pprint(STUDENTS.find_one({'name':'michelle'}))
#she's gone!
##USE WITH CARE!

#everyone can now add themselves into the studnets collection with whatever fields they like, experiment!

#takeaway: mongo doesn't care what you put in there. not everyone needs to agree before what the fields should be!

#let's do some NLP (not really, that's tomorrow :-))
#grab some article from the web and copy the text into ipython
#count all the words of the article and put them into the "article_word_counts" collection

WORD_COUNTS = db['article_word_counts']
article_url='https://techcrunch.com/2017/05/25/watch-spacexs-falcon-heavy-booster-static-test-fire/'
count_doc = {'article_url':article_url,'musk':5,'falcon':7,'rocket':3,'and':45,'heavy':2,'space':11}
WORD_COUNTS.insert(count_doc)

pp.pprint(WORD_COUNTS.find_one({'article_url':article_url}))

#how great is it not to have to know what the fields will be!

#Best practices note:  I wouldn't actually do it this way but save all article fields that are likely to exist across articles on the top level and word counts in a dictionary within the dicitonary such as:
"""
count_doc = {
"url":"...",
"title":"blablah",
"author":"peter",
"date":dt(2017,5,31),
"counts":{"musk":5,"rocket":7,...}
}
"""

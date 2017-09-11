# conda install pymongo
import pymongo

mongodb_uri = 'your_mongodb_uri_here (or set to None for localhost)'
mc = pymongo.MongoClient(mongodb_uri)  # Create MongoClient instance
db = mc[pymongo.uri_parser.parse_uri(mongodb_uri)['database']]  # Specify the database to work with
collection_name = 'mongodb_lecture'  # Specify the collection name to work with
coll = db[collection_name]  # Get a collection instance
# Now we have a collection instance, ready to play with...

# Clear up previous lecture cruft if needed:
# result = coll.delete_many({})
# print(result.deleted_count)

# coll.find_one()
# coll.find().count()
# coll.save({'test': 1})
# coll.find_one()
# coll.find().count()
# coll.update({'test': 1}, {'test': 2})
# coll.find_one()
# coll.find().count()

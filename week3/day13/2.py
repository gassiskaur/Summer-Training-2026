from pymongo import MongoClient


uri = "mongodb+srv://user:ilovedyourtea@summertraining.uncw3yu.mongodb.net/?appName=summertraining"
client = MongoClient(uri)

#accesing the database

db= client['db101']
names= db.list_collection_names()
print(names)

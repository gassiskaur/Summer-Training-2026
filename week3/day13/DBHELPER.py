from pymongo import MongoClient


uri = "mongodb+srv://user:ilovedyourtea@summertraining.uncw3yu.mongodb.net/?appName=summertraining"
client = MongoClient(uri)

#accesing the database

db = client['db101']
names= db.list_collection_names()
print(names)


class DBHelper:
    def __init__(self,db_name='db101'):
        uri= "mongodb+srv://user:ilovedyourtea@summertraining.uncw3yu.mongodb.net/?appName=summertraining"
        self.client= MongoClient(uri)
        self.db_name=self.client[db_name]
        print('DBHELPER CONNECTION CREATED')

    def select_collection(self, collection_name='users'):
        self.collection=db[collection_name]
        print('DBHELPER COLLECTION SELECTED')


    def save(self, document):
        inserted_id = self.collection.insert_one(document)
        print("Doc saved: id: ", inserted_id)


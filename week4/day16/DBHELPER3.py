from pymongo import MongoClient


uri = "mongodb+srv://user:ilovedyourtea@summertraining.uncw3yu.mongodb.net/?appName=summertraining"
client = MongoClient(uri)

#accesing the database

db = client['db101']

#function names are a personal choice but .collection and .client etc are functions of mongodb and cant be changed 

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


    def retrieve(self,condition=None):
        result = self.collection.find(condition)
        print('Doc retrieved, result: ', result)
    
        for document in result:
            print (document) 

        return result 
    
    def update(self, condition=None, document_to_update=None):
        result = self.collection.update_one(
            condition,
            {
                '$set': document_to_update
            }
        )
        print('[DBHelper] Document Updated', result)


    def delete(self, condition):
        result = self.collection.delete_one(condition)
        print('[DBHelper] Document Deleted', result)
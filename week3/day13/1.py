from pymongo import MongoClient
uri = "mongodb+srv://user:ilovedyourtea@summertraining.uncw3yu.mongodb.net/?appName=summertraining"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
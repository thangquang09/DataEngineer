from pymongo import MongoClient

user = "AdminCherry"
password = "090924"
host = "localhost"


# create the connection url

connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

client = MongoClient(connecturl)

db = client["training"]

mongodb_glossary = db["mongodb_glossary"]

print("Inserting Documents")

mongodb_glossary.insert_many([
    {
        "database":"a database contains collections"
    },
    {
        "collection":"a collection stores the documents"
    },
    {
        "document":"a document contains the data in the form of key value pairs."
    }
]
)

print("Querying Documents")
documents = mongodb_glossary.find()

print("Printing Documents")
for doc in documents:
    print(doc)

client.close()
from pymongo import MongoClient
client = MongoClient('mongodb+srv://jyh9017:1234@cluster0.o9uxjjp.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name':'bob',
    'age':27
}

db.users.insert_one(doc)
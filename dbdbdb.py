from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://jyh9017:1234@cluster0.o9uxjjp.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

doc = {
    'name':'bob',
    'age':27
}

db.users.insert_one(doc)
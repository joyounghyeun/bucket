from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://jyh9017:1234@cluster0.o9uxjjp.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('teaaaaaaaaam.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    name_receive = request.form['name_give']
    # teamName_receive = request.form['teamName_give']

    bucket_list = list(db.bucket.find({}, {'_id': False}))
    count = len(bucket_list) + 1

    doc = {
        'num': count,
        'bucket': bucket_receive,
        'done': 0,
        'name': name_receive,
        'teamName': 0
    }
    db.bucket.insert_one(doc)

    return jsonify({'msg': '댓글 완료!'})


@app.route("/bucket/del", methods=["POST"])
def comment_del():
    num_receive = request.form['num_give']

    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'del': 1}})

    return jsonify({'msg': '삭제 완료!'})


@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.bucket.find({}, {'_id': False}))

    return jsonify({'bucket': bucket_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)


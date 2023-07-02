import json

from bson import ObjectId
from bson.json_util import dumps

from flask import Flask, json, jsonify, request
from flask_cors import CORS

from src import db, env

app = Flask(__name__)
CORS(app)


@app.route('/api/blog', methods=['GET'])
def get_blog():
    objava = dumps(db.proces.objava.find())
    return json.loads(objava)


@app.route('/api/blog', methods=['POST'])
def add_blog():
    data = request.get_json()
    db.proces.objava.insert_one(data)
    return 'Blog added successfully'


@app.route('/api/blog/<_id>', methods=['GET', 'POST'])
def get_blog_id(_id):
    objava = dumps(db.proces.objava.find_one({'_id': ObjectId(_id)}))
    return json.loads(objava)


@app.route('/api/blog/delete/<_id>', methods=['DELETE'])
def delete_blog(_id):
    if _id is not None:
        db.proces.objava.delete_one({'_id': ObjectId(_id)})
        return jsonify({"message": "Blog izbrisanm uspešno"})
    else:
        return jsonify({"error": "Blog ne obstaja"})


if __name__ == '__main__':
    # db.drop()
    # db.seed()
    app.run(host='0.0.0.0', port=env.PORT, debug=True)

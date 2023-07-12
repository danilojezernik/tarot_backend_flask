import json
import os

from bson import ObjectId
from bson.json_util import dumps
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from werkzeug.security import generate_password_hash, check_password_hash

from src import db, env

app = Flask(__name__)
CORS(app)

app.secret_key = env.SECRET_KEY
jwt = JWTManager(app)
db_username = os.getenv('UPORABNIK')
db_geslo = os.getenv('GESLO')


@app.route('/api/blog', methods=['GET'])
def get_blog():
    objava = dumps(db.proces.objava.find())
    return json.loads(objava)


@app.route('/api/blog/<_id>', methods=['GET', 'POST'])
def get_blog_id(_id):
    objava = dumps(db.proces.objava.find_one({'_id': ObjectId(_id)}))
    return json.loads(objava)


@app.route("/api/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    if username != db_username or password != db_geslo:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route('/api/blog_pregled', methods=['GET'])
@jwt_required()
def get_blog_pregled():
    return json.loads(dumps(db.proces.objava.find()))


@app.route('/api/blog', methods=['POST'])
@jwt_required()
def add_blog():
    data = request.get_json()
    if data is not None:
        db.proces.objava.insert_one(data)
        return jsonify({"message": "Objava uspešno dodana!"})


@app.route('/api/admin')
@jwt_required()
def get_admin():
    return jsonify({'msg': 'Loged in!'})


@app.route('/api/blog/delete/<_id>', methods=['DELETE'])
@jwt_required()
def delete_blog(_id):
    db.proces.objava.delete_one({'_id': ObjectId(_id)})
    return jsonify({"message": "Blog izbrisanm uspešno"})


@app.route('/api/blog/edit/<_id>', methods=['POST'])
@jwt_required()
def update_blog(_id):
    data = request.get_json()
    result = db.proces.objava.update_one({'_id': ObjectId(_id)}, {'$set': data})
    if result.modified_count > 0:
        updated_document = db.proces.objava.find_one({'_id': ObjectId(_id)})
        updated_document['_id'] = str(updated_document['_id'])
        return jsonify({"message": "Objava uspešno posodobljena", "updated_document": updated_document})
    else:
        return jsonify({"error": "Objava bloga ni uspela!"})


if __name__ == '__main__':
    # db.drop()
    # db.seed()
    app.run(host='0.0.0.0', port=env.PORT, debug=True)

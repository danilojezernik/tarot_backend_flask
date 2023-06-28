import json
from bson.json_util import dumps

from flask import Flask, json
from flask_cors import CORS

from src import db, env

app = Flask(__name__)
CORS(app)


@app.route('/api/blog', methods=['GET'])
def get_blog():
    objava = dumps(db.proces.objava.find())
    return json.loads(objava)


if __name__ == '__main__':
    db.drop()
    db.seed()
    app.run(host='0.0.0.0', port=env.PORT, debug=True)

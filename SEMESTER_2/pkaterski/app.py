from flask import Flask, jsonify
from bson.json_util import ObjectId
from pymongo import MongoClient
import json

class ObjectIdEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(MyEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = ObjectIdEncoder

client = MongoClient(port=27017)
db = client["bmi_proj"]


@app.route("/clinical")
def clinical_all():
    data = list(db.clinical.find())
    return dumps(data)

@app.route("/clinical/<id>")
def clinical(id):
    data = db.clinical.find_one({'id': id})
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'no such entry'}), 404

@app.route("/rnaseq")
def rnaseq_all():
    data = list(db.rnaseq.find())
    return jsonify(data)

@app.route("/rnaseq/<id>")
def rnaseq(id):
    data = db.rnaseq.find_one({'id': id})
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'no such entry'}), 404

@app.route("/mirseq")
def mirseq_all():
    data = list(db.mirseq.find())
    return jsonify(data)

@app.route("/mirseq/<id>")
def mirseq(id):
    data = db.mirseq.find_one({'id': id})
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'no such entry'}), 404

@app.route("/cnvsnp")
def cnvsnp_all():
    data = list(db.cnvsnp.find())
    return jsonify(data)

@app.route("/cnvsnp/<id>")
def cnvsnp(id):
    data = db.cnvsnp.find_one({'id': id})
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'no such entry'}), 404


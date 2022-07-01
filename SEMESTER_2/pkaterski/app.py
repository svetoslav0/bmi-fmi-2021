from flask import Flask, jsonify, request
from bson.json_util import ObjectId
from pymongo import MongoClient
from pymongo.results import InsertManyResult
import json

class ObjectIdEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, InsertManyResult):
            return str(obj)
        return super(ObjectIdEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = ObjectIdEncoder

client = MongoClient(port=27017)
db = client["bmi_proj"]


@app.route("/clinical")
def clinical_all():
    data = list(db.clinical.find())
    return jsonify(data)

@app.route("/clinical/<id>")
def clinical(id):
    data = db.clinical.find_one({'id': id})
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'no such entry'}), 404

def insert_data(col):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        my_json = request.json
        if not isinstance(json, list):
            my_json = [my_json]
        try:
            res = db[col].insert_many(my_json)
            return jsonify(res.inserted_ids)
        except:
            return 'Something bad happened :(', 500
    else:
        return 'Content-Type not supported!', 400

def update_data(col, id):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_query = {'id': id}
        json_values = { '$set' : request.json }
        try:
            res = db[col].update_one(json_query, json_values)
            return jsonify(res.raw_result)
        except:
            return 'Something bad happened :(', 500
    else:
        return 'Content-Type not supported!', 400

def delete_data(col, id):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_query = {'id': id}
        try:
            res = db[col].delete_one(json_query)
            return jsonify(res.raw_result)
        except:
            return 'Something bad happened :(', 500
    else:
        return 'Content-Type not supported!', 400

@app.route("/clinical", methods = ['POST'])
def clinical_create():
    return insert_data('clinical')

@app.route("/clinical/<id>", methods = ['PUT'])
def clinical_update(id):
    return update_data('clinical', id)

@app.route("/clinical/<id>", methods = ['DELETE'])
def clinical_delete(id):
    return delete_data('clinical', id)

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

@app.route("/rnaseq", methods = ['POST'])
def rnaseq_create():
    return insert_data('rnaseq')

@app.route("/rnaseq/<id>", methods = ['PUT'])
def rnaseq_update(id):
    return update_data('rnaseq', id)

@app.route("/rnaseq/<id>", methods = ['DELETE'])
def rnaseq_delete(id):
    return delete_data('rnaseq', id)

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

@app.route("/mirseq", methods = ['POST'])
def mirseq_create():
    return insert_data('mirseq')

@app.route("/mirseq/<id>", methods = ['PUT'])
def mirseq_update(id):
    return update_data('mirseq', id)

@app.route("/mirseq/<id>", methods = ['DELETE'])
def mirseq_delete(id):
    return delete_data('mirseq', id)

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

@app.route("/cnvsnp", methods = ['POST'])
def cnvsnp_create():
    return insert_data('cnvsnp')

@app.route("/cnvsnp/<id>", methods = ['PUT'])
def cnvsnp_update(id):
    return update_data('cnvsnp', id)

@app.route("/cnvsnp/<id>", methods = ['DELETE'])
def cnvsnp_delete(id):
    return delete_data('cnvsnp', id)


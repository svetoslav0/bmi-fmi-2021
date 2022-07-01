from flask import Flask, jsonify, request
from bson.json_util import ObjectId
from pymongo import MongoClient
from pymongo.results import InsertManyResult
import json

from sklearn.linear_model import Ridge
from sklearn.exceptions import NotFittedError
import numpy as np

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

@app.route("/patient-data/<id>", methods = ['GET'])
def patient_data(id):
    res = {}
    res['clinical'] = db.clinical.find_one({'id': id})
    res['rnaseq']   = db.rnaseq.find_one  ({'id': id})
    res['mirseq']   = db.mirseq.find_one  ({'id': id})
    res['cnvsnp']   = db.cnvsnp.find_one  ({'id': id})
    return jsonify(res)

def map_stage(stage):
    if stage == "stage i":    return 1
    if stage == "stage ia":   return 1.3
    if stage == "stage ib":   return 1.6
    if stage == "stage ii":   return 2
    if stage == "stage iia":  return 2.3
    if stage == "stage iib":  return 2.6
    if stage == "stage iii":  return 3
    if stage == "stage iiia": return 3.3
    if stage == "stage iiib": return 3.6
    if stage == "stage iv":   return 4
    if stage == None:         return 0.5

def map_stage_t(stage):
    if stage == "t1"  : return 1
    if stage == "t1a" : return 1.3
    if stage == "t1b" : return 1.6
    if stage == "t2"  : return 2
    if stage == "t2a" : return 2.3
    if stage == "t2b" : return 2.6
    if stage == "t3"  : return 3
    if stage == "t3a" : return 3.3
    if stage == "t3b" : return 3.6
    if stage == "t4"  : return 4
    if stage == "tx"  : return 0.5
    if stage == None  : return 0.5

def map_stage_n(stage):
    if stage == "n0"  : return 0
    if stage == "n1"  : return 1
    if stage == "n1a" : return 1.3
    if stage == "n1b" : return 1.6
    if stage == "n2"  : return 2
    if stage == "n2a" : return 2.3
    if stage == "n2b" : return 2.6
    if stage == "n3"  : return 3
    if stage == "n3a" : return 3.3
    if stage == "n3b" : return 3.6
    if stage == "n4"  : return 4
    if stage == "nx"  : return 0.5
    if stage == None  : return 0.5

def map_stage_m(stage):
    if stage == "m0"  : return 0
    if stage == "m1"  : return 1
    if stage == "m1a" : return 1.3
    if stage == "m1b" : return 1.6
    if stage == "m2"  : return 2
    if stage == "m2a" : return 2.3
    if stage == "m2b" : return 2.6
    if stage == "m3"  : return 3
    if stage == "m3a" : return 3.3
    if stage == "m3b" : return 3.6
    if stage == "m4"  : return 4
    if stage == "mx"  : return 0.5
    if stage == None  : return 0.5

def exists(x):
    return x != None

model = Ridge(alpha=1.0)

def converta_data(row, only_x = False):
    yearstobirth          = None
    vitalstatus           = None
    daystodeath           = None
    daystolastfollowup    = None
    daystolastknownalive  = None

    if not only_x:
        yearstobirth          = row['yearstobirth']
        vitalstatus           = row['vitalstatus']
        daystodeath           = row['daystodeath']
        daystolastfollowup    = row['daystolastfollowup']
        daystolastknownalive  = row['daystolastknownalive']
    
    pathologicstage       = row['pathologicstage']
    pathologyTstage       = row['pathologyTstage']
    pathologyNstage       = row['pathologyNstage']
    pathologyMstage       = row['pathologyMstage']
    
    numberpackyearssmoked = row['numberpackyearssmoked']

    # |-------------------|
    # |set variable values|
    # |-------------------|
    days_to_live = None
    if not only_x:
        if vitalstatus:
            days_to_live = daystodeath
        elif daystolastknownalive:
            days_to_live = daystolastknownalive
        else:
            days_to_live = daystolastfollowup

    age     = yearstobirth or 50
    stage   = map_stage(pathologicstage)
    stage_t = map_stage_t(pathologyTstage)
    stage_n = map_stage_n(pathologyNstage)
    stage_m = map_stage_m(pathologyMstage)
    if exists(age) and exists(stage)and exists(stage_t) and exists(stage_n) and exists(stage_m):
        X = [age, stage, stage_t, stage_n, stage_m]
        if only_x:
            return X, None
        elif exists(days_to_live):
            Y = (days_to_live)
            return X, Y
        else:
            raise Exception('Unable to convert')
    else:
       raise Exception('Unable to convert') 


def fit_model():
    data = db.clinical.find()
    training_data_X = []
    training_data_Y = []
    for row in data:
        try:
            x, y = converta_data(row)

            training_data_X.append(x)
            training_data_Y.append(y)

        except:
            print('missing data in row: ' + str(row))
            pass
    model.fit(np.array(training_data_X), np.array(training_data_Y))

@app.route("/update-model", methods = ['POST'])
def update_model():
    try:
        fit_model()
        return 'ok', 200
    except:
        return 'training error occured', 500


@app.route("/predict", methods = ['POST'])
def predict():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        my_json = request.json
        try:
            x, _ = converta_data(my_json, only_x=True)

            res = None
            try:
               res = model.predict([x]) 
            except NotFittedError as e:
                fit_model()
                res = model.predict([x])

            return jsonify({ 'predicted days to death:' : res[0] })
        except:
            return 'Something bad happened :(', 500
    else:
        return 'Content-Type not supported!', 400


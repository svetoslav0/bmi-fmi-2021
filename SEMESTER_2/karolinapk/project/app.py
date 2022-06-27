from flask import Flask, request, Response
from flask_mongoengine import MongoEngine
from model.brca_data import BRCAData
from ml.pipeline import MLPipeline
from apscheduler.schedulers.background import BackgroundScheduler
import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': '127.0.0.1:27017',
    'db': 'CANCER_DATA',
    'alias': 'default'
}

db = MongoEngine(app)

pipeline = MLPipeline()
pipeline.load_model()

scheduler = BackgroundScheduler()
scheduler.start()

scheduler.add_job(
    func=lambda: pipeline.run_pipeline(json.loads(BRCAData.objects().to_json())),
    trigger='cron',
    hour='9',
    minute='45')

@app.route('/add_data', methods=['POST'])
def add_data():
    body = request.get_json()
    data = BRCAData(**body).save()
    return "Successfully added data with id {}".format(data.id), 201

@app.route('/bulk_add', methods = ['POST'])
def bulk_add():
    body = request.get_json()
    instances = [BRCAData(**data) for data in body]
    size = len(instances)
    BRCAData.objects.insert(instances, load_bulk=False)
    return "Successfully added buck data with size {}".format(size), 201

@app.route('/get_data', methods=['GET'])
def get_data():
    data = BRCAData.objects().to_json()
    return Response(data, mimetype="application/json", status=200)

@app.route('/get_data/<id>', methods=['GET'])
def get_data_by_id(id):
    data = BRCAData.objects(id=id).to_json()
    return Response(data, mimetype="application/json", status=200)

@app.route('/delete_data/<id>', methods=['DELETE'])
def delete_data(id):
    BRCAData.objects.get(id=id).delete()
    return 'Successfully deleted object', 200


@app.route('/update_data/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    BRCAData.objects.get(id=id).update(**body)
    return 'Successfully updated object', 200

@app.route('/predict_cancer', methods=['POST'])
def predict():
    body = request.get_json()
    result = pipeline.predict(body)
    response = dict()
    response['prediction'] = result[0]
    response['unit'] = "days"
    return response, 200

if __name__ == '__main__':
    app.run()

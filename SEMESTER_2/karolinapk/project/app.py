from flask import Flask, request, Response
from flask_mongoengine import MongoEngine
from model.brca_data import BRCAData

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': '127.0.0.1:27017',
    'db': 'CANCER_DATA',
    'alias': 'default'
}

db = MongoEngine(app)

@app.route('/add_data', methods=['POST'])
def add_data():
    body = request.get_json()
    data = BRCAData(**body).save()
    return "Successfully added data with id {}".format(data.id), 201


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

if __name__ == '__main__':
    app.run()

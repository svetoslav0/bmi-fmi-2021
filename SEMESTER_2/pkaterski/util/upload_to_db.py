from pymongo import MongoClient
from utils import HOME
import json

client = MongoClient(port=27017)
db = client["bmi_proj"]

#with open(f'{HOME}/Downloads/data/clinical.json', 'r') as data:
#    clinical_json = json.load(data)
#    col = db["clinical"]
#    col.insert_many(clinical_json)
#    print('OK: clinical_json')

with open(f'{HOME}/Downloads/data/rnaseq.json', 'r') as data:
    rnaseq_json = json.load(data)
    col = db["rnaseq"]
    col.insert_many(rnaseq_json)
    print('OK: rnaseq_json')

with open(f'{HOME}/Downloads/data/mirseq.json', 'r') as data:
    mirseq_json = json.load(data)
    col = db["mirseq"]
    col.insert_many(mirseq_json)
    print('OK: mirseq_json')

with open(f'{HOME}/Downloads/data/cnvsnp.json', 'r') as data:
    cnvsnp_json = json.load(data)
    col = db["cnvsnp"]
    col.insert_many(cnvsnp_json)
    print('OK: cnvsnp_json')

#print(clinical_json)
#print(rnaseq_json)
#print(mirseq_json)
#print(cnvsnp_json)

#print(client.list_database_names())
#print(db.local.estimated_document_count())




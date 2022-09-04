import json
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts='https://localhost:9200', verify_certs=False, http_auth=('elastic', 'tRN_8KMUel4rA_=VNE*2'))


file = open('../initial_data.json')

data = json.load(file)

for case in data:
    diagnoses = case['diagnoses']

    for diagnose in diagnoses:
        treatments = diagnose['treatments']

        for treatment in treatments:
            treatment_id = treatment['treatment_id']

            print('Creating doc {}'.format(treatment_id))

            resp = es.index(index="treatments", id=treatment_id, document=treatment)
            print(resp)
            print('Created')

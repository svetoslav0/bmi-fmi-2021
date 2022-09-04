import json
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts='https://localhost:9200', verify_certs=False, http_auth=('elastic', 'tRN_8KMUel4rA_=VNE*2'))

file = open('../initial_data.json')

data = json.load(file)

for case in data:
    exposures = case['exposures']

    for exposure in exposures:
        exposure_id = exposure['exposure_id']

        print('Creating doc {}'.format(exposure_id))

        resp = es.index(index='exposures', id=exposure_id, document=exposure)
        print(resp)
        print('Created')

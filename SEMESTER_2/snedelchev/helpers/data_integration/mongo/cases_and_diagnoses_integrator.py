import json
import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
database = mongo_client['kirc']
cases_collection = database['cases']
diagnoses_collection = database['diagnoses']


file = open('../initial_data.json')

data = json.load(file)

for case in data:
    exposure_ids = list()

    for exposure in case['exposures']:
        exposure_ids.append(exposure['exposure_id'])

    case['exposure_ids'] = exposure_ids
    del case['exposures']

    diagnosis_ids = list()
    for diagnose in case['diagnoses']:
        diagnosis_ids.append(diagnose['diagnosis_id'])

        treatment_ids = list()

        for treatment in diagnose['treatments']:
            treatment_ids.append(treatment['treatment_id'])

        diagnose['treatment_ids'] = treatment_ids
        del diagnose['treatments']

        diagnose_response = diagnoses_collection.insert_one(diagnose)
        print(diagnose_response)

    case['diagnosis_ids'] = diagnosis_ids
    del case['diagnoses']

    response = cases_collection.insert_one(case)
    print(response)

import csv
import json
from utils import HOME

def csv_to_json(file_path):
    path_arr = file_path.split('.csv')
    if len(path_arr) > 2:
        err  = 'invalid file naming (has to end in .csv'
        err += ' and no other .csv should be present)'
        raise Exception(err)

    file_path = path_arr[0]

    jsonArray = []
      
    with open(file_path + '.csv', encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 

        for row in csvReader: 
            # Convert `NA` text to None (null in json)
            for key in row:
                if row[key].lower() == 'na':
                    row[key] = None
                try:
                    row[key] = int(row[key])
                except:
                    try:
                        row[key] = float(row[key])
                    except:
                        pass

            jsonArray.append(row)
  
    with open(file_path + '.json', 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          

csv_to_json(f'{HOME}/Downloads/data/clinical')
csv_to_json(f'{HOME}/Downloads/data/rnaseq'  )
csv_to_json(f'{HOME}/Downloads/data/mirseq'  )
csv_to_json(f'{HOME}/Downloads/data/cnvsnp'  )


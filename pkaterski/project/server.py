from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

url = 'https://rest.ensembl.org/'
hs = { "content-type": "application/json" }

@app.route('/v1/sequence/gene/<id>/exons')
def sequence_gene(id='ENST00000645032'):

    seq_req = requests.get(url = f'{url}sequence/id/{id}', headers = hs)
    exp_req = requests.get(url = f'{url}lookup/id/{id}?expand=1', headers = hs)

    follow_exon_seq = request.args.get('exon_seq') == '1'


    if seq_req.ok and exp_req.ok:
        seq = ''
        exons = ''
        try:
            seq = seq_req.json()['seq']
            exp_json = exp_req.json()

            def extract_exon(ex):
                exon = { 'start': ex['start'], 'end': ex['end'], 'id': ex['id'] }
                return exon

            def get_exon_seq(ex):
                ex_id = ex['id']
                try:
                    r = requests.get(url = f'{url}sequence/id/{ex_id}', headers = hs).json()
                    ex['seq'] = r['seq']
                    return ex
                except Exception as e:
                    return ex



            if 'Exon' in exp_json:
                exons = list(map(extract_exon, exp_json['Exon']))
            else:
                exons = sum(
                        list(map(lambda x: list(map(extract_exon, x['Exon'])),
                             exp_json['Transcript'])),
                        [])
                exons = list(set(exons))
        except Exception as e:
            return f'error {e}'

        if follow_exon_seq:
            exons = list(map(get_exon_seq, exons))

        return jsonify(
                seq=seq,
                exons=exons,
        )

    return f'{url} returned an error (sequence request: {seq_req.text}, \
            expanded request: {exp_req.text}'









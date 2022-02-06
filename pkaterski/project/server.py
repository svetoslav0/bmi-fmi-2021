from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

url = 'https://rest.ensembl.org/'

@app.route('/v1/sequence/gene/<id>/')
def sequence_gene(id='ENST00000645032'):

    hs = { "content-type": "application/json" }
    seq_req = requests.get(url = f'{url}sequence/id/{id}', headers = hs)
    exp_req = requests.get(url = f'{url}lookup/id/{id}?expand=1', headers = hs)


    if seq_req.ok and exp_req.ok:
        seq = ''
        exons = ''
        try:
            seq = seq_req.json()['seq']
            exp_json = exp_req.json()

            def extract_exon(ex):
                ex_id = ex['id']
                exon = { 'start': ex['start'], 'end': ex['end'], 'id': ex_id }
                try:
                    r = requests.get(url = f'{url}sequence/id/{ex_id}', headers = hs).json()
                    exon['seq'] = r['seq']
                    return exon
                except Exception as e:
                    return exon


            if 'Exon' in exp_json:
                exons = list(map(extract_exon, exp_json['Exon']))
            else:
                exons = sum(
                        list(map(lambda x: list(map(extract_exon, x['Exon'])),
                             exp_json['Transcript'])),
                        [])
        except Exception as e:
            return f'error {e}'

        return jsonify(
                seq=seq,
                exons=exons,
        )

    return f'{url} returned an error (sequence request: {seq_req.text}, \
            expanded request: {exp_req.text}'
    # gc_content = request.args.get('gc_content', '')
    # swap = ''
    # if gc_content:
    #     swap = request.args.get('swap', '')
    # content_type = request.args.get('content-type', '')
    # return f"The id is {escape(id)}, gc_content={gc_content}, swap={swap}, content_type={content_type}"









from flask import Flask, jsonify, request
from Bio.SeqUtils import GC
from Bio import SeqIO
import requests

app = Flask(__name__)

@app.route('/v1/sequence/gene/<id>')
def get_exons(id):
    # id = 'ENSG00000157764'
    # id = '123'

    seq_response = requests.get('https://rest.ensembl.org/sequence/id/' + id, headers={"Content-Type": "application/json"})
    seq_json = seq_response.json()

    seq_id = seq_json['id']
    seq = seq_json['seq']
    description = seq_json['desc']

    exons_response = requests.get('https://rest.ensembl.org/lookup/id/' + id + '?expand=1', headers={"Content-Type": "application/json"})
    exons = exons_response.json()['Transcript'][0]['Exon']

    return jsonify(
        seq=seq,
        exons=exons
    )

@app.route('/v1/sequence/gene/<id>/gc_content')
def get_gene_data(id):
    args = request.args
    swap = args.get('swap')

    seq_response = requests.get('https://rest.ensembl.org/sequence/id/' + id, headers={"Content-Type": "application/json"})
    seq_json = seq_response.json()
    seq = seq_json['seq']
    gc = GC(seq)

    swap_sequence = seq
    if swap:
        first = swap[0]
        second = swap[2]
        swap_sequence = seq.upper().replace(first.upper(), second.lower()).replace(second.upper(), first.lower()).upper()

    return jsonify(
        seq=seq,
        gc_content=gc,
        swap_sequence=swap_sequence
    )

@app.route('/v1/sequence/<id>')
def get_seq(id):
    seq_response = requests.get('https://rest.ensembl.org/sequence/id/' + id, headers={"Content-Type": "text/x-fasta"})
    fasta_response = seq_response.text

    seq_id = fasta_response.split('\n')[0]
    seq = ''.join(fasta_response.split('\n')[1:])
    print(seq)

    return jsonify(
        id=seq_id,
        seq=seq
    )

from flask import Flask, request, jsonify
import requests

app = Flask("__main__")


@app.route('/v1/sequence/gene/<id>')
def gene_with_exons(id):
    sequence_response = requests.get('https://rest.ensembl.org/sequence/id/' + id, headers={"Content-Type": "application/json"})
    sequence = sequence_response.json()['seq']

    exons = requests.get('https://rest.ensembl.org/lookup/id/' + id + '?expand=1', headers={"Content-Type": "application/json"})

    return jsonify(
        seq=sequence,
        exons=exons.json()['Transcript'],
    )

@app.route('/v1/sequence/gene/<id>/gc')
def gene(id):
    args = request.args
    swap = args.get('swap')

    sequence_response = requests.get('https://rest.ensembl.org/sequence/id/' + id, headers={"Content-Type": "application/json"})
    sequence = sequence_response.json()['seq']

    if swap is None:
        swap = 'A:T'

    base_one = swap[0]
    base_two = swap[2]

    sequence_swapped = None
    sequence = sequence.replace('T', 'a').replace('A', 't')

    if base_one == 'A' and base_two == 'T':
        sequence_swapped = sequence.replace('T', 'a').replace('A', 't')

    if base_one == 'A' and base_two == 'C':
        sequence_swapped = sequence.replace('C', 'a').replace('A', 'c')

    if base_one == 'A' and base_two == 'G':
        sequence_swapped = sequence.replace('G', 'a').replace('A', 'g')



    if base_one == 'T' and base_two == 'A':
        sequence_swapped = sequence.replace('T', 'a').replace('A', 't')

    if base_one == 'T' and base_two == 'C':
        sequence_swapped = sequence.replace('T', 'c').replace('C', 't')

    if base_one == 'T' and base_two == 'G':
        sequence_swapped = sequence.replace('T', 'a').replace('A', 't')



    if base_one == 'C' and base_two == 'A':
        sequence_swapped = sequence.replace('C', 'a').replace('A', 'c')

    if base_one == 'C' and base_two == 'T':
        sequence_swapped = sequence.replace('C', 't').replace('T', 'c')

    if base_one == 'C' and base_two == 'G':
        sequence_swapped = sequence.replace('C', 'g').replace('G', 'c')


    if base_one == 'G' and base_two == 'A':
        sequence_swapped = sequence.replace('A', 'g').replace('G', 'a')

    if base_one == 'G' and base_two == 'T':
        sequence_swapped = sequence.replace('T', 'g').replace('G', 't')

    if base_one == 'G' and base_two == 'C':
        sequence_swapped = sequence.replace('C', 'g').replace('G', 'c')

    return jsonify(
        seq=sequence.upper(),
        gc=GC(sequence),
        sequence_swapped=sequence_swapped.upper()
    )

@app.route('/v1/sequence/<id>')
def seq(id):
    sequence_response = requests.get('https://rest.ensembl.org/sequence/id/' + id, headers={"Content-Type": "text/x-fasta"})
    fasta = sequence_response.text
    fasta = fasta.split('\n')

    sequence_metadata = fasta[0]
    fasta.pop(0)

    sequence = ''.join(fasta)

    return jsonify(
        id=sequence_metadata,
        seq=sequence
    )

def GC(sequence):
    gc = sequence.count('G') + sequence.count('C')
    try:
        return gc * 100.0 / len(sequence)
    except ZeroDivisionError:
        return 0.0

app.run()
        

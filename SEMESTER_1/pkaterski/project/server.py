from flask import Flask, request, Response, jsonify
import requests
from Bio.SeqUtils import GC
import textwrap as tw
from Bio.Seq import Seq
import Bio.Data.CodonTable

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
                except Exception:
                    return ex



            if 'Exon' in exp_json:
                exons = list(map(extract_exon, exp_json['Exon']))
            else:
                exons = sum(
                        list(map(lambda x: list(map(extract_exon, x['Exon'])),
                             exp_json['Transcript'])),
                        [])
                #exons = list(set(exons))
        except Exception as e:
            return f'error {e}', 500

        if follow_exon_seq:
            exons = list(map(get_exon_seq, exons))

        return jsonify(
                seq=seq,
                exons=exons,
        )

    return f'{url} returned an error (sequence request: {seq_req.text}, \
            expanded request: {exp_req.text}', 500


@app.route('/v1/sequence/gene/<id>/swap')
def swap(id):
    swap = request.args.get('swap')
    gc_content = request.args.get('gc_content') == 'true'

    bases = ['A', 'T', 'G', 'C']

    if not swap or len(swap) != 3\
    or swap[1] != ':'\
    or swap[0].upper() not in bases\
    or swap[2].upper() not in bases:
        return 'invalid swap arg', 400


    try:
        seq = requests.get(url = f'{url}sequence/id/{id}', headers = hs)\
            .json()['seq'].upper()
        a = ord(swap[0].upper())
        b = ord(swap[2].upper())
        swapped = seq.translate({ a: b, b: a })
        res = { 'seq': seq, 'swap_sequence': swapped}
        if gc_content:
            res['gc_content'] = GC(seq)

        return jsonify(res)
    except Exception as e:
        return f"an error occured {e}", 500


@app.route('/v1/sequence/<id>/content')
def content(id):
    xhs = { "content-type": "text/x-fasta" }
    ctype = request.args.get('content-type')
    try:
        seq = requests.get(url = f'{url}sequence/id/{id}', headers = xhs)
        if not ctype:
            return 'missing content-type', 400
        if ctype.lower() == 'fasta':
            return Response(seq.text, mimetype='text/plain')
        elif ctype.lower() == 'x-fasta':
            lines = seq.text.split('\n')
            xseq = { 'id': lines[0], 'seq': ''.join(lines[1:]) }
            return xseq
        else:
            return f"invalid content-type: {ctype}", 400
    except Exception as e:
        return f"an error occured {e}", 500



codon_table = Bio.Data.CodonTable.unambiguous_dna_by_id[28]

def orf(dna_seq):
    starts = codon_table.start_codons
    stops = codon_table.stop_codons
    codon_dict = codon_table.forward_table

    def seq_to_proteins(_seq):
        protein_seqs = []
        l = len(_seq)
        seq = _seq[0 : l - l % 3]
        seq_codons = tw.wrap(seq, 3)
        lc = len(seq_codons)

        current_protein = ''
        for i in range(lc):
            if seq_codons[i] in starts:
                for j in range(i, lc):
                    if seq_codons[j] not in stops:
                        sq = seq_codons[j]
                        current_protein += codon_dict[sq] if sq in codon_dict else 'Unk'
                    else:
                        protein_seqs.append(current_protein)
                        current_protein = ''
                        break
        return protein_seqs

    rev_comp = str(Seq(dna_seq).reverse_complement())

    res = sum(
            [
                seq_to_proteins(dna_seq),
                seq_to_proteins(dna_seq[1:]),
                seq_to_proteins(dna_seq[2:]),
                seq_to_proteins(rev_comp),
                seq_to_proteins(rev_comp[1:]),
                seq_to_proteins(rev_comp[2:]),
                ],
            [])

    return list(set(res))


@app.route('/v1/sequence/<id>/orf')
def get_orf(id):
    try:
        seq = requests.get(url = f'{url}sequence/id/{id}', headers = hs)\
            .json()['seq'].upper()

        return jsonify(orf(seq))
    except Exception as e:
        return f"an error occured {e}", 500



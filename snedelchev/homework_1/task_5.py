from Bio.Seq import Seq


def get_dna_to_reversed_rna(source_filename, new_filename):
    with open(source_filename, 'r') as content:
        dna_seq = Seq(content.readline())
        result = str(dna_seq.transcribe())[::-1]

        with open(new_filename, 'w') as f:
            f.write(result)


get_dna_to_reversed_rna('data/dna_chromosome_1.seq', 'rna_reversed.seq')

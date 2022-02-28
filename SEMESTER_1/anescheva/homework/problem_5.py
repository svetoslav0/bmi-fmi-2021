from Bio.Seq import Seq

with open('dna_chromosome_1.seq', 'r') as seq:
    seq = Seq(seq.readline())
    rna = str(seq.transcribe())
    reverse = rna[::-1]

    with open('rna_reversed.seq', 'w') as result:
        result.write(reverse)
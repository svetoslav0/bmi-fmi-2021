from collections import Counter
from Bio.Seq import Seq
from Bio import SeqIO


# Да се намери честотата на срещане на “А” Аденин в секвенцията: ATAGTGGGAAGATTTATA
def tast1():
    seq = 'ATAGTGGGAAGATTTATA'
    print(Counter(seq)['A'])
    print(Seq(seq).count('A'))


# Да се прочете секвенция от файл [data/sequence_1.seq] и да се запише в обратна последователност в нов файл с име [reverse_sequence_1.seq]
def task2():
    lines = []
    with open('data/sequence_1.seq', 'r') as ls:
        for line in ls:
            lines.append(line.replace('\n', ''))
    rev_ = list(map(lambda x: x[::-1]+'\n', lines[::-1]))
    rev = ''.join(rev_)
    with open('data/reverse_sequence_1.seq', 'w') as f:
        f.write(rev)


# Да се прочете секвенцията(Fasta формат) от файл [data/fasta_seq_1.fa] и да се намери честотата на срещане на “Т” в секвенцията(15т.)
def task3():
    ts = 0
    for record in SeqIO.parse('data/fasta_seq_1.fa', 'fasta'):
        ts += record.seq.count('T')
    print(ts)

# Да се прочете секвенция от файл [data/dna_chromosome_1.seq] и да се разменят всички символте “А” → “T”, “T” → “A” . Резултатът да се записва в нов файл с име [dna_chromosome_solve_1.seq] (20т.)
def task4():
    lines = []
    with open('data/dna_chromosome_1.seq', 'r') as ls:
        for line in ls:
            lines.append(line.translate({ ord('A'): ord('T'), ord('T'): ord('A') }))

    with open('data/dna_chromosome_solve_1.seq', 'w') as f:
        for line in lines:
            f.write(line)

# Да се прочете DNA секвенция от файл [data/dna_chromosome_1.seq] и да се преобразува във RNA като резултатът се запише в нов файл като секвенцията е в обратен ред. (15т.)
def task5():
    lines = []
    with open('data/dna_chromosome_1.seq', 'r') as ls:
        for line in ls:
            lines.append(line.replace('\n', ''))

    seq_dna = Seq(''.join(lines))
    seq_rna = seq_dna.transcribe()[::-1]
    with open('data/rna_chromosome_1_reversed.seq', 'w') as f:
        f.write(str(seq_rna))


# Да се реши следата задача от rosalind -> http://rosalind.info/problems/subs/
def subs(s, t):
    ls = len(s)
    lt = len(t)
    locations = []

    for i in range(ls):
        full_match = True
        for j in range(lt):
            if s[i + j] != t[j]:
                full_match = False
                break

        if full_match:
            locations.append(i + 1)

    return locations


def task6():
    print(subs('GATATATGCATATACTT', 'ATAT'))
    print(subs('AUGCUUCAGAAAGGUCUUACG', 'U'))
    print(subs('AUGCUUCAGAAAGGUCUUACG', 'UGCU'))


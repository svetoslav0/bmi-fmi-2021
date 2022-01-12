from Bio.Seq import Seq


def get_frequency(seq):
    dna = Seq(seq)
    return dna.count('A')


print(get_frequency('ATAGTGGGAAGATTTATA'))
from Bio import SeqIO

for seq in SeqIO.parse('fasta_seq_1.fa', 'fasta'):
    print(seq.seq.count('T'))
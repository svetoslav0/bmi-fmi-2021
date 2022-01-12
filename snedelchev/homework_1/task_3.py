from Bio import SeqIO


def get_frequency_in_file(filename, file_format, key):
    for record in SeqIO.parse(filename, file_format):
        return record.seq.count(key)


print(get_frequency_in_file('data/fasta_seq_1.fa', 'fasta', 'T'))

def reverse_seq(filename):
    with open(filename, 'r') as f:
        seq = f.readline()
        return seq[::-1]


print(reverse_seq('data/sequence_1.seq'))

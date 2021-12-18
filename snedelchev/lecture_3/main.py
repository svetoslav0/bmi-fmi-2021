from Bio import SeqIO

sequences = []

for seq_entry in SeqIO.parse('seq.fasta', 'fasta'):
    sequences.append(str(seq_entry.seq))

sorted_seq = sorted(sequences, key=len)
shortest_seq = sorted_seq[0]
rest_seq = sorted_seq[1:]

pattern = ''
for i in range(len(shortest_seq)):
    for j in range(i, len(shortest_seq)):
        best_pattern = shortest_seq[i:j + 1]

        found = False
        for current_seq in rest_seq:
            if best_pattern in current_seq:
                found = True
            else:
                found = False
                break

        if found and len(best_pattern) > len(pattern):
            pattern = best_pattern

print(pattern)

with open('dna_chromosome_1.seq', 'r') as seq:
    seq = seq.readline()
    seq = seq.replace('T', '$')
    seq = seq.replace('A', '%')
    seq = seq.replace('$', 'A')
    seq = seq.replace('%', 'T')

    with open('dna_chromosome_solve_1.seq', 'w') as result:
        result.write(seq)
    
def exchange_t_and_a(source_filename, new_filename):
    with open(source_filename, 'r') as content:
        seq = content.readline()
        result = seq.replace('T', 'a').replace('A', 't').upper()

        with open(new_filename, 'w') as f:
            f.write(result)


exchange_t_and_a('data/dna_chromosome_1.seq', 'dna_chromosome_solve_1.seq')

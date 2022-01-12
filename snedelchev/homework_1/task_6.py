def get_mofit_positions(dna, sub_dna):
    positions = []
    for i in range(len(dna)):
        if dna[i] == sub_dna[0]:
            if dna[i:i + len(sub_dna)] == sub_dna:
                positions.append(i + 1)

    return positions


dna_source = 'GATATATGCATATACTT'
sub_dna_source = 'ATAT'

positions_list = get_mofit_positions(dna_source, sub_dna_source)
print(' '.join(map(str, positions_list)))

import re

dna_string = input('DNA input: ')

a_count = len(re.findall(r'A', dna_string))
c_count = len(re.findall(r'C', dna_string))
g_count = len(re.findall(r'G', dna_string))
t_count = len(re.findall(r'T', dna_string))

print(f'{a_count} {c_count} {g_count} {t_count}')

from Transcribing_DNA_into_RNA import transcription
from Translating_RNA_into_Protein import translation
from Complementing_a_Strand_of_DNA import complementer


def find_protein(dna):
    proteins = set()
    for i in range(len(dna)):
        if dna[i:i + 3] == 'ATG':
            DNAlst = []
            for j in range(i, len(dna), 3):
                DNAlst.append(dna[j:j + 3])
            if 'TAG' in DNAlst or 'TGA' in DNAlst or 'TAA' in DNAlst:
                proteins.add(translation(transcription(dna[i:])))

    for i in range(len(dna)):
        if complementer(dna)[i:i + 3] == 'ATG':
            DNAlst = []
            for j in range(i, len(dna), 3):
                DNAlst.append(dna[j:j + 3])
            if 'TAG' in DNAlst or 'TGA' in DNAlst or 'TAA' in DNAlst:
                proteins.add(translation(transcription(complementer(dna)[i:])))
    proteins = list(proteins)
    return proteins


with open('rosalind_orf3.txt', 'r') as file:
    content = file.read()

dna_source = ''
for i in range(1, len(content.splitlines())):
    dna_source += content.splitlines()[i]

lst = find_protein(dna_source)
for i in lst:
    print(i)

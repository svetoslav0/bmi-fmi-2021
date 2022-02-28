from collections import defaultdict
from collections import Counter
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import GC

for seqEntry in SeqIO.parse("fastam.fasta","fasta"):
    print("DNA = " + seqEntry.seq)
    print("RNK = " + seqEntry.seq.transcribe())
    print(GC(seqEntry.seq))


seq = Seq("GATGGAACTTGACTACGTAAATT")
print(seq.transcribe())

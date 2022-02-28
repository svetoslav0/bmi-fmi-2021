
class SEQ: 
    def GC(self, val1, val2):
        print("SEQ")
        pass

    def __init__(self, seq = 'GGGGGGGGGGG'):
        self.seq = seq
        pass
    pass

class DNA(SEQ):
    def reverce(self):
        pass

    def GC(self, val1, val2):
        print("DNA")

dna = DNA()
dna.GC(1, 2)

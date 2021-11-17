def debug(function):
    def wrapper(*args, **kwargs):  
        print("Arguments:", args, kwargs)  
        return function(*args, **kwargs)
    return wrapper

@debug
def foo(a, b, c=1):  
    return (a + b) * c


class RNA: 
    def __init__(self, seq):
        print(seq)
        pass

    def __contains__(self, key):
        return True

rna1 = RNA("GTUU")
rna2 = RNA("GTTU")







class DNA:
    def __init__(self, seq):
        self.seq = seq

    def __eq__(self, o: object) -> bool:
        return True
        pass
    def __or__(self, t):
        return False
        pass
    pass


# dna1 = DNA("seq")
# dna2 = DNA("seq2")

# if dna1 == dna2:
#     print("true")
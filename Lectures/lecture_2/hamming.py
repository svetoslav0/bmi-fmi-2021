from scipy.spatial import distance

print(distance.jaccard("GCTATGACCGTGCCATTCATTAGAAGTGTTCTAAATCCGTTAGGCCGGCT", "GCTATGACCGCGCCATTAATTAGAAGTGTTCTAAATCCGTTAGGCCGGCT"))
print(distance.hamming("GCTATGACCGTGCCATTCATTAGAAGTGTTCTAAATCCGTTAGGCCGGCT", "GCTATGACCGCGCCATTAATTAGAAGTGTTCTAAATCCGTTAGGCCGGCT"))
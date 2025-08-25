from itertools import permutations

def permuteUnique(s: str):
    
    perms = set(permutations(s))
    
    return ["".join(p) for p in perms]


print(permuteUnique("abc"))   
print(permuteUnique("aab"))  
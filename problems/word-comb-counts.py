from string import ascii_uppercase
from functools import lru_cache

@lru_cache(maxsize=None)
def combs(length):
    if length == 1: return set(ascii_uppercase)
    
    s_names = combs(length-1)
    curr_names = set()
    for name in s_names:
        for c in ascii_uppercase:
            for i in range(length+1):
                curr_names.add(name[:i] + c + name[i:])
            
    return curr_names

cs = combs(1) | combs(2) | combs(3) | combs(4) | combs(5)
print("fin")

cs_2 = cs.copy()
for key in ['IF', 'OR', 'AND', 'THEN', 'GOTO']:
    for name in cs:
        if key in name: cs_2.discard(name)

print(len(cs_2))

# Copyright © 2014 Bart Massey
# Function: return the list of permutations of a set

# Strategy:
# To find the permutations of s:
#    if s is the empty set
#        return a list containing the empty list
#    build up a result by picking each element e
#      in s and prepending e to each element of perm(s \ {e})
#    return the result

def perms(s):
    # base case: empty set
    if len(s) == 0:
        return [[]]

    # inductive case
    result = []
    for e in s:
        t = s.difference({e})
        pt = perms(t)
        for p in pt:
            result += [[e] + p]
    return result

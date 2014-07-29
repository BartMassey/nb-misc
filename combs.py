# Copyright © 2014 Bart Massey
# Give a list of all sets of k items drawn from a set of n items

def combs(s, k):
    n = len(s)
    if k > n:
        return []
    if k == n:
        return [s]
    if k == 0:
        return [set()]
    t = s.copy()
    e = t.pop()
    cs = combs(t, k - 1)
    ecs = []
    for c in cs:
        ecs += [c.union({e})]
    return ecs + combs(t, k)

if __name__ == "__main__":
    print(combs(set(range(3)), 2))
    print(combs(set(range(4)), 3))
    print(len(combs(set(range(52)), 5)))

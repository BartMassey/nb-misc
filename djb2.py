# Copyright © 2014 Bart Massey
# Hash function djb2 on strings.

# http://www.cse.yorku.ca/~oz/hash.html
def djb2(s):
    h = 5381
    for c in s:
        h = (33 * ord(c) + h) % 65536
    return h

def djb2_improved(s):
    h = 5381
    n = 0
    for c in s:
        h = (32609 * ord(c) * n + h) % 65536
        n += 1
    return h

def terrible_hash(s):
    if s == "":
        return 0
    return ord(s[0]) % 2

# Given a hash function and a set s of strings, return
# the number of times that the hash
# one of the strings represents the
# hash of some other string.
def collision_count(hash_function, to_check):
    count = 0
    seen = set()
    for s in to_check:
        h = hash_function(s)
        if h in seen:
            count += 1
        else:
            seen = seen.union({h})
    assert len(to_check) - len(seen) == count
    return count

if __name__ == "__main__":
    assert collision_count(terrible_hash, {'a', 'b', 'c', 'd'}) == 2

    chars = set()
    for c in range(32, 128):
        chars = chars.union({chr(c)})
    print(collision_count(terrible_hash, chars))
    print(collision_count(djb2, chars))
    print(collision_count(djb2_improved, chars))

    print()

    chars = set()
    for c1 in range(32, 128):
        for c2 in range(32, 128):
            chars = chars.union({chr(c1) + chr(c2)})
    print(collision_count(terrible_hash, chars))
    print(collision_count(djb2, chars))
    print(collision_count(djb2_improved, chars))

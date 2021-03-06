# Very partial replacement for Python random module
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

# PRNG seed.
s = 12

def randrange(p1, p2=None):
    global s

    # Analyze parameters to set bounds.
    if p2 == None:
        lower = 0
        upper = p1
    else:
        lower = p1
        upper = p2
    
    # Compute the result by normalizing bounds.
    r = (s % (upper - lower)) + lower

    # Update the seed.
    s = (s * 55) % 251

    return r

if __name__ == "__main__":
    for _ in range(10):
        print(randrange(15))

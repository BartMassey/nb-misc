# Generate all permutations and try something with each
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

def try_perms(source_set, eval_function):

    def complete_perm(current_elements, partial_permutation):
        if len(current_elements) == 0:
            eval_function(partial_permutation)
            return
        for e in current_elements:
            complete_perm(current_elements.difference({e}), \
                          partial_permutation + [e])

    complete_perm(source_set, [])

class Found(Exception):

    def __init__(self, result):
        self.result = result

def check_first_zero(p):
    if p[0] == 0:
        raise Found(p)

try:
    try_perms(set(range(50)), check_first_zero)
except Found as e:
    print(e.result)

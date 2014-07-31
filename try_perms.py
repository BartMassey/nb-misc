# Copyright © 2014 Bart Massey
# Generate all permutations and try something with each

def try_perms(source_set, eval_function):

    def complete_perm(current_elements, partial_permutation):
        if len(current_elements) == 0:
            eval_function(partial_permutation)
            return
        for e in current_elements:
            complete_perm(current_elements.difference({e}), \
                          partial_permutation + [e])

    complete_perm(source_set, [])

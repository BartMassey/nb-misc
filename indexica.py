# Copyright © 2014 Bart Massey
# Range function with better arguments.

def indexica(start, end, increment):
    assert increment != 0
    if increment < 0:
        tmp = start
        start = end + increment
        end = tmp + increment
    result = []
    i = start
    while i != end:
        result += [i]
        i += increment
    return result
    

print(indexica(3, 10, 1))
print(indexica(3, 10, -1))

for i in indexica(0, 1000000, 1):
    print(i)

# Copyright © 2014 Bart Massey
# Range function with better arguments.

def indexica(start, end, increment):
    assert increment != 0
    if increment < 0:
        tmp = start
        start = end + increment
        end = tmp + increment
    i = start
    while i != end:
        yield i
        i += increment

if __name__ == "__main__":
    print(list(indexica(3, 10, 1)))
    print(list(indexica(3, 10, -1)))

    for i in indexica(0, 100, 1):
        print(i)

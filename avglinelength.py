# Copyright © 2014 Bart Massey
# File input demo. Prints the average line length of a
# textfile.

from sys import stdin, stderr, argv

if len(argv) <= 1:
    infile = stdin
elif len(argv) == 2:
    infile = open(argv[1], "r")
else:
    print("usage: %s [file]" % (argv[0],), file=stderr)
    exit(1)

nlines = 0
total_ll = 0
for line in infile:
    nlines += 1
    total_ll += len(line)
if nlines == 0:
    print("empty file", file=stderr)
    exit(1)
print(total_ll / nlines)

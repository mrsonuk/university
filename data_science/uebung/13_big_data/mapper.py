import sys

for line in sys.stdin:
    n = line.strip()
    m = n.split()
    print('%s\t%s' % (m[0], m[1]))

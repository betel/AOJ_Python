import sys
for x in sys.stdin.readlines():
    l = map(int,x.split())
    l.remove(l[0])
    a,b,c = l
    if c**2 == a**2 + b**2 :
        print "YES"
    else:
        print "NO"
n = raw_input()
l = map(int,raw_input().split())
l.reverse()
s = [str(x) for x in l]
print " ".join(s)
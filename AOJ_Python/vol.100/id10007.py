while True:
    l = map(int,raw_input().split())
    if l==[0,0]:
        break
    l.sort()
    s = [str(x) for x in l]
    print " ".join(s)
"""
while True:
    try:
        a,b = map(int,raw_input().split())
        print len(str(a+b))
    except EOFError:
        break
"""
import sys
for i in sys.stdin.readlines():
    a,b = map(int,i.split())
    print len(str(a+b))
l=[]
while True:
    try:
        l.append(input())
    except EOFError:
        break
l.sort(reverse = True)
for i in range(3):
    print l[i]
while True:
    a,op,b = raw_input().split()
    a,b = int(a),int(b)
    if op=="?": break
    if op=="+": print a+b
    if op=="-": print a-b
    if op=="*": print a*b
    if op=="/": print a/b
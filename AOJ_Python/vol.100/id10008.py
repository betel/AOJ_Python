from decimal import Decimal
a,b = map(int, raw_input().split())
d = a / b
r = a % b
f = Decimal(a)/Decimal(b)
print d,r,f
a, b, c = map(int, input().split())
may = a
if b > may: may = b
if c > may: may = c
men = a
if b < men: men = b
if c < men: men = c
central = 0
if a > b and a < c or a < b and a > c: central = a
elif b > a and b < c or b < a and b > c: central = b
elif c > a and c < b or c < a and c > b: central = c
elif a == b: central=a
else :central = c
print(men, central, may)
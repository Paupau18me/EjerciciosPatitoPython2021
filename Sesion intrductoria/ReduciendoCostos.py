n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    central = 0
    if a > b and a < c or a < b and a > c:
        central = a
    elif b > a and b < c or b < a and b > c:
        central = b
    elif c > a and c < b or c < a and c > b:
        central = c
    print('case ',i+1,': ',central, sep='')
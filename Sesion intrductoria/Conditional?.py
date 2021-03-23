n, a, b = map(int, input().split())
op = input()
m1 = n % a == 0
m2 = n % b == 0
if op == 'AND':
    if m1 and m2:
        print('SI')
    else:
        print('NO')
else:
    if m1 or m2:
        print('SI')
    else:
        print('NO')
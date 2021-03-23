a, b = map(str, input().split('.'))
if len(a) == 1:
    print('  {}'.format(a), end='.')
elif len(a) == 2:
    print(' {}'.format(a), end='.')
else:
    print('{}'.format(a), end='.')
b = float('0.'+b)
print(str(round(b,3))[-3:])


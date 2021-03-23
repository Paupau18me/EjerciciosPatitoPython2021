a, b, c ,d = map(int, input().split())
if a < c:
    a1 = a
    b1 = b
    a2 = c
    b2 = d
else:
    a1 = c
    b1 = d
    a2 = a
    b2 = b
print('[',end='')
if b1 < a2:
    pass
else:
    if a1<=a2<=b1:
        print(a2,end=',')
    if b1 >= b2:
        print(b2, end='')
    else:
        print(b1, end='')
print(']',end='')





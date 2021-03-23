n = int(input())
for i in range(n):
    cad = input()
    condi = cad.count('U')>=1 and cad.count('M')>=1 and cad.count('S')>=1 and cad.count('A')>=1 and cad.count('I')>=1 and cad.count('C')>=2 and cad.count('P')>=1
    if condi:
        print('ES POSIBLE')
    else:
        print('NO ES POSIBLE')
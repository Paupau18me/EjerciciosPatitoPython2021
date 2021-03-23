import sys
for linea in sys.stdin:
    n = int(linea)
    if n == 0:
        print('error')
    else:
        ini = 4
        res = 2
        for j in range(n-1):
            print(ini, end=' ')
            ini = (ini*3) - res
            res = res+2
        print(ini, end='')
        print()



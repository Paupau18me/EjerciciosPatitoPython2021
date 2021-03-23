def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
n = int(input())
i = 0
sw = True
j = 2
a = 1
cntS = 2
while i < n:
    if es_primo(j):
        if sw:
            print(a,'/',j,sep='')
            sw = False
        else:
            print(j,'/',a,sep='')
            sw = True
        a = a + cntS
        cntS = cntS +1
        i= i+1
    j = j + 1



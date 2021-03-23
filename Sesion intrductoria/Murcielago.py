n = int(input())
cad = [0 for i in range(n+1)]
for i in range(n):
    cad[i] = input()
for i in range(n):
    cad[i] = cad[i].replace('M', '0')
    cad[i] = cad[i].replace('U', '1')
    cad[i] = cad[i].replace('R', '2')
    cad[i] = cad[i].replace('C', '3')
    cad[i] = cad[i].replace('I', '4')
    cad[i] = cad[i].replace('E', '5')
    cad[i] = cad[i].replace('L', '6')
    cad[i] = cad[i].replace('A', '7')
    cad[i] = cad[i].replace('G', '8')
    cad[i] = cad[i].replace('O', '9')
for i in range(n):
    print(cad[i])
    


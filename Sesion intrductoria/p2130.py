cad = input()
cad_aux = cad.split()
vowels = ['a', 'e', 'i', 'o', 'u']
vow = ''
cons = ''
for i in range(len(cad_aux)):
    if cad_aux[i][0] in vowels:
        vow = vow + cad_aux[i]+ ' '
    else:
        cons = cons + cad_aux[i]+ ' '
print(vow[:-1])
print(cons[:-1])
print(cad)
print('Espacios en blanco:',len(cad_aux)-1)
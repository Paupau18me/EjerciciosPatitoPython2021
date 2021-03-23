def ordenamientoBurbujaCorto(unaLista):
    global cnt
    cnt = 0
    intercambios = True
    numPasada = len(unaLista)-1
    while numPasada > 0 and intercambios:
       intercambios = False
       for i in range(numPasada):
           if unaLista[i]>unaLista[i+1]:
               intercambios = True
               temp = unaLista[i]
               unaLista[i] = unaLista[i+1]
               unaLista[i+1] = temp
               cnt = cnt+1
       numPasada = numPasada-1
def ordenamientoBurbuja(unaLista):
    global cnt
    cnt = 0
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if int(unaLista[i])>int(unaLista[i+1]):
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
                cnt = cnt +1
n = int(input())
for k in range(n):
    n2 = input()
    lista = input().split()
    ordenamientoBurbuja(lista)
    print(cnt)




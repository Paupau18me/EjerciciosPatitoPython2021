casos = int(input())
for i in range(casos):
    n = int(input())
    entrada = [int(x) for x in input().split()]
    for elem in reversed(entrada):
        print(elem, end=' ')
    print()


#print(*reversed(v))
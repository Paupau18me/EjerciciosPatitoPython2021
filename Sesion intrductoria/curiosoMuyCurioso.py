def factorial(n):
    if (n <= 1) :return 1
    return n * factorial(n - 1)
def sumFactoriales(n):
    total = 0
    for j in range(len(n)):
        total = total + int(n[j])
    return total
cases = int(input())
for i in range(cases):
    n = input()
    if sumFactoriales(n) == int(n):
        print('Y')
    else
        print('N')


def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            
primos ='2357'
n = int(input())
for i in range(n):
    num = input()
    resul = ''
    for j in range(len(num)):
        if num[j] in primos:
            resul = resul + num[j]
    print(resul if resul != '' else '0')



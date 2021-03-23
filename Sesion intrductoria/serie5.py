import math
def serie(n):
    t = 1
    c = 0
    for i in range(n):
        if c < t:
            c = c + 1
        else:
            t = t + 1
            c = 1
    return t

def fibo(n):
    a = 1
    b = 0
    for i in range(n):
        f = a + b
        a = b
        b = f
    return f
N = int(input())
sum = 0
for i in range(1, N+1):
    sum = sum + math.factorial(fibo(i))/serie(i)
print("{:.2f}".format(sum))

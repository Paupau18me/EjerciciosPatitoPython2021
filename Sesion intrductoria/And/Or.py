a, b , n = map(int, input().split())
print(bin(a)[2::])
print("",bin(b)[2::])
print("",bin(a&b)[2::])
'''
if n == 1:
    print(a & b)
else:
    print(a | b)
'''
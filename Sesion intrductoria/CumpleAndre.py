cases = int(input())
for i in range(cases):
    n, h, v = map(int, input().split(' '))
    p1 = 4 * (h) * (v)
    p2 = 4 * (n - h) * (v)
    p3 = 4 * (h) * (n - v)
    p4 = 4 * (n - h) * (n - v)
    print(max(p1, max(p2, max(p3, p4))))

for i in range(int(input())):
    n, op = map(int, input().split())
    if op == 1: print("{:.02f}".format(n - (n * 0.12)))
    else: print("{:.02f}".format(n - (n * 0.17)))
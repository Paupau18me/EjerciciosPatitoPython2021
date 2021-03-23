while True:
    try:
        n = input()
        sum = 0
        for i in range(len(n)):
            sum = sum + int(n[i])
        print('La suma de los digitos de {} es {}'.format(n, sum))
    except EOFError:
        break
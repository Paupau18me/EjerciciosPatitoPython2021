while(True):
    try:
        n = input()
        sw = True
        for i in range(len(n)):
            if n[i] in '47':
                sw = True
            else:
                sw = False
                pass
        if sw == True:
            print('YES')
        else:
            if  int(n) % 4 == 0 or int(n) % 7 == 0 :
                print('YES')
            else:
                print('NO')
    except EOFError:
        break

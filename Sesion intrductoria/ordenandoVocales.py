n = int(input())
vowels = 'aeiou'
for i in range(n):
    cad = input()
    cnt = [cad.count('a'), cad.count('e'), cad.count('i'), cad.count('o') ,cad.count('u')]
    sw = 0
    for j in range(len(cad)):
        if cad[j] in vowels:
            if sw < cnt[0]:
                cad = cad[:len(cad)-j-1]+ 'a' +cad[len(cad)-j:]
                sw = sw+1
            elif sw < cnt[0] + cnt[1]:
                cad = cad[:len(cad) - j - 1] + 'e' + cad[len(cad) - j:]
                sw = sw + 1
            elif sw < cnt[0] + cnt[1]+ cnt[2]:
                cad = cad[:len(cad) - j - 1] + 'i' + cad[len(cad) - j:]
                sw = sw + 1
            elif sw < cnt[0] + cnt[1]+ cnt[2] + cnt[3]:
                cad = cad[:len(cad) - j - 1] + 'o' + cad[len(cad) - j:]
                sw = sw + 1
            elif sw < cnt[0] + cnt[1]+ cnt[2]+ cnt[3] +cnt[4]:
                cad = cad[:len(cad) - j - 1] + 'u' + cad[len(cad) - j:]
                sw = sw + 1
    print(cad)

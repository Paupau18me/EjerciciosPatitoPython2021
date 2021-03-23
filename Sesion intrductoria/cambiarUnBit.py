
n, posicion = map(int, input().split())
n_binario = bin(n)
n_binario = n_binario[2:]
print(int(n_binario[:len(n_binario)-posicion-1]+ '1' +n_binario[len(n_binario)-posicion:],2), end=' ')
print(int(n_binario[:len(n_binario)-posicion-1]+ '1' +n_binario[len(n_binario)-posicion:], 2) if n_binario[-(posicion+1)] == '0' else int(n_binario[:len(n_binario) - posicion - 1] + '0' + n_binario[len(n_binario) - posicion:], 2))

'''
if n_binario[-(posicion+1)] == '0':
    n_binario = n_binario[:len(n_binario)-posicion-1]+ '1' +n_binario[len(n_binario)-posicion:]
else:
    n_binario = n_binario[:len(n_binario) - posicion - 1] + '0' + n_binario[len(n_binario) - posicion:]
print(int(aux, 2), int(n_binario, 2))
'''

'''
s = "ABCDEFGH"
#s[1] = 'a'
#s[-1]='b'

s=s[0:1]+'a'+s[2:]
print(s)

'''

'''
x, y = map(int, input().split())
print(x|(1<<y),x^(1<<y))

'''

def rotar_izquierda(cadena, posiciones):
  return cadena[posiciones:] + cadena[:posiciones]
def rotar_derecha(cadena, posiciones):
  return rotar_izquierda(cadena, -posiciones)
n, pos = map(int, input().split())
cad = input().split(' ')
cad_aux = ''
for i in range(len(cad)):
    cad_aux= cad_aux + cad[i]
if pos > 0:
    cad = (rotar_derecha(cad_aux, pos))
else:
    cad = (rotar_izquierda(cad_aux, -pos))
for j in range(len(cad)-1):
    print(cad[j], end=' ')
print(cad[len(cad)-1], end='')

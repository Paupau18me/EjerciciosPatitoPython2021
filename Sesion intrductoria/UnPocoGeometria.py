import sys
from fractions import Fraction
for linea in sys.stdin:
    AB, AC, BD = map(int, linea.split())
    resultado = Fraction(AC*AB,BD-AC)
    if "/" in str(resultado):
        print(resultado)
    else:
        print("{}/{}".format(resultado,1))

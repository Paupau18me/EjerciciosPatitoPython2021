import math
x1, y1, x2, y2 = map(float, input().split())

distancia = math.sqrt(math.pow(x1-x2, 2)+ math.pow(y1-y2, 2))

print("{:.02f}".format(round(distancia,2)))


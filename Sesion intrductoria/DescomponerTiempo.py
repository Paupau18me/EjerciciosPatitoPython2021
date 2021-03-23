
total_seg= int(input())
# 1hora = 3600seg
# 1minuto = 60seg

h = total_seg//3600  # total_seg//3600= 1 || total_seg%3600 = 61
m = (total_seg%3600) // 60
s = (total_seg%3600) % 60
print(h, m, s)
h, m, s = map(int, input().split())
total_seg = 0
s += 1 # s = s+1
m = m*60
h = h*3600
total_seg = s+m+h
h = total_seg // 3600
m = (total_seg % 3600) // 60
s = (total_seg % 3600) % 60
print("{:02d}:{:02d}:{:02d}".format((h%24),m,s))
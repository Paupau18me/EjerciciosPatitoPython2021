n = int(input())
home = input()
for i in range(n):
    origin, destiny = map(str, input().split("->"))
if home == destiny: print('home')
else: print('contest')
#MAL :(

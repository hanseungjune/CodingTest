lst = [[0] * 100 for i in range(100)]

rep = int(input())
for i in range(rep):
  # a: 왼쪽벽과의 거리, b: 아래쪽벽과의 거리
  a, b = map(int, input().split())
  
  for j in range(a, a+10):
    for k in range(b, b+10):
      lst[j][k] = 1

wreath = 0
for l in range(100):
  for m in range(100):
    if lst[l][m] == 1:
      wreath += 1

print(wreath)
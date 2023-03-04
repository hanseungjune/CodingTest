T = int(input())

arr = [[0] * 15 for i in range(15)]

for j in range(1, 15):
  arr[0][j] = j

for a in range(1, 15):
  for b in range(1, 15):
    arr[a][b] = sum(arr[a-1][:b+1])

for t in range(T):
  k = int(input())
  n = int(input())

  print(arr[k][n])

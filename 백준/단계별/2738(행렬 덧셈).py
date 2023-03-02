n, m = map(int, input().split())

lst = [list(map(int, input().split())) for i in range(n)]
arr = [list(map(int, input().split())) for j in range(n)]

for a in range(n):
  for b in range(m):
    lst[a][b] += arr[a][b]
    print(lst[a][b], end=' ')
  print()
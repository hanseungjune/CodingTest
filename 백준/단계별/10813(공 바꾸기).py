n, m = map(int, input().split())

lst = [i for i in range(n+1)]

for j in range(m):
  # a에서 b로
  a, b = map(int, input().split())
  
  prev = lst[a]
  lst[a] = lst[b]
  lst[b] = prev

for k in range(1, len(lst)):
  print(lst[k], end=' ')
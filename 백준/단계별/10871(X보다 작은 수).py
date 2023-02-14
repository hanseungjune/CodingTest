n, x = map(int, input().split())
lst = list(map(int, input().split()))

check = []

for i in range(n):
  if lst[i] < x:
    check.append(lst[i])
  else:
    continue

for j in range(len(check)):
  print(check[j], end=' ')
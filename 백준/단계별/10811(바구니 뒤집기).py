n, m = map(int, input().split())
lst = [i for i in range(n+1)]

for j in range(m):
  a, b = map(int, input().split())
  
  for k in range(n+1):
    # 해당 인덱스 사이일때,
    if a <= k <= b:
      lst_cp = lst[a:b+1]
      idx = -1
      for ele in range(a, b+1):
        lst[ele] = lst_cp[idx]
        idx -= 1
      else:
        break
    else:
      continue

for res in range(1, len(lst)):
  print(lst[res], end=' ')
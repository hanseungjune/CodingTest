tc = int(input())

for i in range(tc):
  n, *lst = map(int, input().split())
  avg = sum(lst)/n
  
  success = 0
  for j in range(n):
    if avg < lst[j]:
      success += 1
    else:
      continue
  
  ans = round(success/n*100, 3)
  print(f'{ans:.3f}%')
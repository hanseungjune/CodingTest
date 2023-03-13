n = int(input())
result = []

for i in range(1, n+1):
  num_lst = list(map(int, str(i)))
  sum_num = i + sum(num_lst)
  
  if sum_num == n:
    result.append(i)

if not result:
  print(0)
else:
  print(min(result))


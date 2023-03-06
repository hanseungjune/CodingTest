a, b = map(int, input().split())

lst = set()
i = 1
while True:
  if a % i == 0:
    if a == i:
      lst.add(i)
      break
    lst.add(i)
  i += 1

sort_lst = sorted(list(lst))

if len(sort_lst) >= b:
  print(sort_lst[b-1])
else:
  print(0)
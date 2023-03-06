while True:
  a = int(input())

  if a == -1:
    break

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
  arr = sort_lst[:len(sort_lst)-1]
  if sum(arr) == a:
    print(f'{a} = {arr[0]}', end=' ')
    for i in range(1, len(arr)):
      print(f'+ {arr[i]}', end=' ')
    print()
  else:
    print(f'{a} is NOT perfect.')
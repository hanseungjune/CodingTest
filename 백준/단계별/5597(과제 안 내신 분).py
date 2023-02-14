lst = [i for i in range(1, 31)]

for i in range(28):
  lst.remove(int(input()))

sort_lst = sorted(lst)

for j in sort_lst:
  print(j)


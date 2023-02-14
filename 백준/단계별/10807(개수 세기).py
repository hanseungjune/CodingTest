from collections import Counter

cnt = int(input())
lst = list(map(int, input().split()))
search = int(input())

lst_cnt = dict(Counter(lst))

if lst_cnt.get(search)==None:
  print(0)
else:
  print(lst_cnt.get(search))
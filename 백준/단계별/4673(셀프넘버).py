def d(num):
  ans = num
  lst = list(str(num))
  for i in range(len(lst)):
    ans += int(lst[i])
  return ans

arr = set([i for i in range(1, 10001)])
sub = set([d(i) for i in range(1, 10001)])
res = sorted(list(arr-sub))

for j in range(len(res)):
  print(res[j])





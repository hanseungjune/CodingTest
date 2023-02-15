num = int(input())
cnt = 0
if num <= 99:
  cnt = num
else:
  cnt = 99
  for i in range(100, num+1):
    lst = list(str(i))
    if int(lst[0]) - int(lst[1]) == int(lst[1]) - int(lst[2]):
      cnt += 1
    else:
      continue

print(cnt)

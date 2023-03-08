import math

num = int(input())

if num == 1:
  exit()
else:
  lst = []
  for i in range(2, int(math.sqrt(num))+1):
    while num % i == 0:
      lst.append(i)
      num //= i
    if num == 1:
      break
  if num > 1:
    lst.append(num)

  for j in range(len(lst)):
    print(lst[j])

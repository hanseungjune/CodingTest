rep = int(input())

number = list(map(int, input().split()))

arr = []
for r in range(rep):
  i = 1
  lst = []
  while True:
    if number[r] % i == 0:
      lst.append(i)
      if i == number[r]:
        arr.append(lst)
        break
    i += 1
    
cnt = 0
for j in arr:
  if len(j) == 2:
    cnt += 1
print(cnt)

    
arr = []

while True:
  a, b = map(int, input().split())
  if (a, b) == (0, 0):
    break
  arr.append(a+b)

for i in range(len(arr)):
  print(arr[i])
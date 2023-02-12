rep = int(input())
arr = []

for i in range(rep):
  a, b = map(int, input().split())
  arr.append([a, b, a+b])

for j in range(rep):
  print(f'Case #{j+1}: {arr[j][0]} + {arr[j][1]} = {arr[j][2]}')
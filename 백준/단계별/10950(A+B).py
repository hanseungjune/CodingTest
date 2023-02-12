rep = int(input())
arr = []
for i in range(rep):
  a, b = map(int, input().split())
  arr.append(a+b)

for j in range(rep):
  print(arr[j])
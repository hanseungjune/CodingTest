import sys

rep = int(sys.stdin.readline())
arr = []
for i in range(rep):
  a, b = map(int, input().split())
  arr.append(a+b)

for j in range(rep):
  print(f"Case #{j+1}: {arr[j]}")
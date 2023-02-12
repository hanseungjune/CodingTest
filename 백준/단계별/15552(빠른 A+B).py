import sys

rep = int(sys.stdin.readline())
arr = []

for i in range(rep):
  a, b = map(int, sys.stdin.readline().split())
  arr.append(a+b)

for j in range(rep):
  print(arr[j])


import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
  a, b = map(int, input().split())
  lst.append((a, b))

lst.sort(key=lambda x: (x[0], x[1]))

for row in lst:
  for col in row:
    print(col, end=' ')
  print()
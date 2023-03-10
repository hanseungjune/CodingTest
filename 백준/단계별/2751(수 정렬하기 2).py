import sys
input = sys.stdin.readline

n = int(input())

# lst = [0] * (1000001)
# for _ in range(n):
#   lst[int(input())] += 1

# for i in range(1000001):
#   for j in range(lst[i]):
#     print(i)

lst = []
for _ in range(n):
  lst.append(int(input()))

lst.sort()

for r in range(n):
  print(lst[r])
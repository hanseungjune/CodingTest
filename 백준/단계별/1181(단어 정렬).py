import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
  word = input().strip()
  lst.append((word, len(word)))

lst.sort(key=lambda x : (x[1], x[0]))

arr = []
for i in lst:
  if i[0] not in arr:
    arr.append(i[0])

for j in arr:
  print(j)
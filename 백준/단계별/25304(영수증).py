result = int(input())
rep = int(input())
ans = 0
for i in range(rep):
  a, b = map(int,input().split())
  ans += (a*b)

if ans==result:
  print('Yes')
else:
  print('No')
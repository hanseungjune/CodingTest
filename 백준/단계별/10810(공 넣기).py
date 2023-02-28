# 바구니 갯수, 몇 번 반복문
n, m = map(int, input().split())

lst = [0] * (n+1)
for i in range(m):
  i, j, k = map(int, input().split())

  for ele in range(i, j+1):
    lst[ele] = k
  
for res in range(1, len(lst)):
  print(lst[res], end=" ")
  
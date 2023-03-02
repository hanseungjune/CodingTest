lst = [list(map(int, input().split())) for i in range(9)]

mx_ele = 0
mr, mc = 0, 0
for i in range(9):
  for j in range(9):
    if mx_ele < lst[i][j]:
      mx_ele = lst[i][j]
      mr, mc = i, j

print(mx_ele)
print(mr+1, mc+1)
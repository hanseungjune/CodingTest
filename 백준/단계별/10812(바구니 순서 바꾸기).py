n, m = map(int, input().split())
# 3,4,5,6,7,8,9
lst = [e for e in range(n+1)]
for rep in range(m):
    i, j, k = map(int, input().split())
    lst_cp = lst[i:j+1]
    for a in range(k-i):
        ele = lst_cp.pop(0)
        lst_cp.append(ele)
    lst[i:j+1] = lst_cp

for b in range(1, len(lst)):
    print(lst[b], end=' ')
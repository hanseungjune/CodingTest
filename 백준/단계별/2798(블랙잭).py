from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
lst = list(combinations(cards, 3))

diff = m
ans = 0
for l in lst:
  if sum(l) <= m and m - sum(l) < diff:
    diff = m - sum(l)
    ans = sum(l) 

print(ans)
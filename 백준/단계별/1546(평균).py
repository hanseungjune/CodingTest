cnt = int(input())
lst = list(map(int, input().split()))
ans = []

for i in range(cnt):
  ans.append(lst[i]/max(lst) * 100)

avg = sum(ans)/cnt

print(avg)
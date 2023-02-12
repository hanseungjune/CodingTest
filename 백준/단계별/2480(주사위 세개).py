from collections import Counter

a, b, c = map(int, input().split())
dices = sorted([a,b,c],reverse=True)

ans = 0
for key, value in dict(Counter(dices)).items():
  if value == 3:
    ans = (10000 + key*1000)
    break
  elif value == 2:
    ans = (1000 + key*100)
    break
  else:
    ans = (dices[0]*100)

print(ans)


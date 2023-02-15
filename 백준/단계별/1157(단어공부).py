from collections import Counter
word = dict(Counter(input().lower()))

cnt = 0
ans = ''
for key, value in word.items():
  if value == max(word.values()):
    cnt += 1
    ans = key
  else:
    continue

if cnt >= 2:
  print('?')
else:
  print(ans.upper())

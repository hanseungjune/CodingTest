rep = int(input())
ans = 0

for i in range(rep):
  word = list(input())
  lst = []

  for j in range(len(word)):
    if j == 0:
      lst.append(word[j])
      continue

    if word[j] == word[j-1]:
      continue
    else:
      lst.append(word[j])
  
  if len(lst) == len(set(lst)):
    ans += 1
  else:
    continue

print(ans)
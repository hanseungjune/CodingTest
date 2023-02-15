alpha = list('abcdefghijklmnopqrstuvwxyz')
alpha_idx = list(-1 for i in range(len(alpha)))
response = list(input())

for i in range(len(response)):
  for j in range(len(alpha)):
    if response[i] == alpha[j] and alpha_idx[j] == -1:
      alpha_idx[j] = i
    else:
      continue

for k in range(len(alpha_idx)):
  print(alpha_idx[k], end=' ')

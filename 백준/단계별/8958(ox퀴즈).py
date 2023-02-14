cnt = int(input())

for i in range(cnt):
  ox = list(input())

  total = 0
  score = 1
  for i in range(len(ox)):
    if ox[i] == 'O':
      total += score
      score += 1
    else:
      score = 1
  
  print(total)
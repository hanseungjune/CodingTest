rep = int(input())
for r in range(rep):
  pow, word = map(str, input().split())

  for i in range(len(word)):
    for j in range(int(pow)):
      print(word[i], end='')
  print()
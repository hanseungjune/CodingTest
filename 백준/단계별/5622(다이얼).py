dial_dict = {
    2:['A','B','C'],
    3:['D','E','F'],
    4:['G','H','I'],
    5:['J','K','L'],
    6:['M','N','O'],
    7:['P','Q','R','S'],
    8:['T','U','V'],
    9:['W','X','Y','Z'],
}

word = list(input())
ans = 0

for i in range(len(word)):
  for key, value in dial_dict.items():
    if word[i] in value:
      ans += (key+1)
    else:
      continue

print(ans)
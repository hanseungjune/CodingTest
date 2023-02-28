num = int(input())
ans = ''

repeat = num//4
while True:
  ans += 'long '
  repeat -= 1
  if repeat == 0:
    break

ans += 'int'

print(ans)
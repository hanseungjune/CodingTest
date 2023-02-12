hour, minutes = map(int, input().split())

# 1~23, 0
# 0~44, 45~59
if hour == 0:
  if minutes <= 44:
    hour = 23
    minutes += 15
  else:
    minutes -= 45
else:
  if minutes <= 44:
    hour -= 1
    minutes += 15
  else:
    minutes -= 45

print(hour, minutes)
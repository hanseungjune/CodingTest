# 1 => 1
# 2, 3, 4, 5, 6, 7 => 6
# 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 => 12

num = int(input())
area = 1
floor = 1
if num == 1:
    print(floor)
else:
  while True:
    area += floor*6
    if num <= area:
       print(floor+1)
       break
    else:
      floor += 1
cnt = int(input())

bags = [-1]
i = -1
while True:
  i += 1
  j = cnt - 5*i
  if j >= 1 and j % 3 == 0:
    bags.append(i+(j//3))
  else:
    if cnt == i*5:
      bags.append(i)
    if i*5 > cnt:
      break
    else:
      continue

if len(bags) == 1:
  print(-1)
else:
  print(min(bags[1:]))

########################### 밑에는 GPT ###############################

n = int(input()) # 배달해야 할 설탕의 무게

bag_count = 0 # 필요한 봉지 개수
while n >= 0:
    if n % 5 == 0: # 5킬로그램 봉지로 나누어 떨어지는 경우
        bag_count += n // 5 # 필요한 봉지 개수 추가
        print(bag_count)
        break
    n -= 3 # 5킬로그램 봉지로 나누어 떨어지지 않는 경우 3킬로그램 봉지 한 개 추가
    bag_count += 1 # 필요한 봉지 개수 추가
else:
    print(-1) # 정확하게 N킬로그램을 배달할 수 없는 경우 -1 출력
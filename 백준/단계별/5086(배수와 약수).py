while True:
  a, b = map(int, input().split())
  if a != 0 and b != 0:
    ans = ''

    # 약수의 경우
    if a != b and b % a == 0:
      ans = 'factor'
    # 배수의 경우 
    elif a != b and a % b == 0:
      ans = 'multiple'
    else:
      ans = 'neither'

    print(ans)
  else:
    break
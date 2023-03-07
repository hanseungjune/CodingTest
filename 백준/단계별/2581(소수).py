import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

lst = [i for i in range(m, n+1)]

arr = []
for num in lst:
  k = 1
  nums = []
  while True:
    if num % k == 0:
      nums.append(k)
      if k == num:
        break
    k += 1
  if len(nums) == 2:
    arr.append(num)

if len(arr) == 0:
  print(-1)
else:
  print(sum(arr))
  print(min(arr))

######################################

# import math

# # M과 N을 입력받음
# M = int(input())
# N = int(input())

# # M부터 N까지의 자연수 중 소수를 찾음
# prime_list = []
# for num in range(M, N+1):
#     if num == 1:
#         continue
#     elif num == 2:
#         prime_list.append(num)
#     else:
#         for i in range(2, int(math.sqrt(num))+1):
#             if num % i == 0:
#                 break
#         else:
#             prime_list.append(num)

# # 소수가 없으면 -1을 출력하고 종료
# if len(prime_list) == 0:
#     print(-1)
# else:
#     # 소수들의 합과 최솟값을 구함
#     prime_sum = sum(prime_list)
#     prime_min = min(prime_list)
    
#     # 결과 출력
#     print(prime_sum)
#     print(prime_min)







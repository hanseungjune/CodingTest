# import sys
# num = int(sys.stdin.readline())
# start = 1
# r, c = 1, 1
# while True:
#   if num == start:
#     print("{}/{}".format(r,c))
#     break
#   # 2개 합이 짝수면, (행이 -1, 열이 +1) => 행이 1이 되면 c += 1
#   if (r+c)%2==0:
#     if r != 1:
#       r -= 1
#     c += 1
#   # 2개 합이 홀수면, (행이 +1, 열이 -1) => 열이 1이 되면 r += 1
#   else:
#     if c != 1:
#       r += 1
#     c -= 1
#   start += 1

input_num = int(input())

line = 0  # 사선 라인
max_num = 0  # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자
while input_num > max_num:
    line += 1  
    max_num += line  

gap = max_num - input_num 
if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line - gap  #분자
    under = gap + 1  #분모
else :  # 사선 라인이 홀수번째 일 때
    top = gap + 1  #분자
    under = line - gap  #분모
print('{}/{}'.format(top, under))

ans = int(input())

if((ans%4==0 and ans%100!=0) or ans%400==0):
  print(1)
else:
  print(0)
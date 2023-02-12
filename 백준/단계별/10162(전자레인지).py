ans = int(input())

fm_cnt, om_cnt, ts_cnt = 0, 0, 0

# 300초 먼저 나누고
if(ans>=300):
  fm_cnt = ans//300
  ans = ans%300
# 60초 나누고
if(ans>=60):
  om_cnt = ans//60
  ans = ans%60
# 10초 나누고
if((ans//10 and not ans%10) or (not ans//10 and (fm_cnt>0 or om_cnt>0) and not ans%10)):
  ts_cnt = ans//10
  print(fm_cnt, om_cnt, ts_cnt)
else:
  print(-1)

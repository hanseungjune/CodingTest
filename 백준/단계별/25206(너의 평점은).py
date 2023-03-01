score_dict ={
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0
}

total_score = 0
total_hour = 0
for i in range(20):
  title, hour, grade = map(str, input().split())
  if grade == 'P':
    continue

  else:
    total_hour += float(hour)
    for key in score_dict.keys():
      if key == grade:
        total_score += float(hour)*score_dict[key]
        break

print("{:.6f}".format(total_score/total_hour))
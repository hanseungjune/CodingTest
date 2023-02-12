import datetime

a, b = map(int, input().split())
c = int(input())

now = datetime.timedelta(hours = a, minutes = b)
cooking = datetime.timedelta(minutes= c)

hour = ((now.seconds+cooking.seconds)//3600)%24 
minute = ((now.seconds + cooking.seconds)//60)%60

print(hour, minute)
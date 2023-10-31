from datetime import datetime
from datetime import timedelta

# from datetime import time
# from datetime import date

# import datetime

# result = dir(datetime)
# result = dir(datetime.time)
# result = dir(datetime.date)

simdi= datetime.now()
simdi= datetime.today()


result= datetime.now()
result= simdi.year
result= simdi.month
result= simdi.month
result= simdi.day
result= simdi.hour
result= simdi.minute
result= simdi.second
result= datetime.ctime(simdi)
result = datetime.strftime(simdi,"%Y")
result = datetime.strftime(simdi,"%X")
result = datetime.strftime(simdi,"%d")
result = datetime.strftime(simdi,"%a")
result = datetime.strftime(simdi,"%b")
result = datetime.strftime(simdi,"%m")
result = datetime.strftime(simdi,"%Y %B %A")

# t= "21 Nisan 2019"
# gun,ay,yıl= t.split()
# print(gun)
# print(ay)
# print(yıl)

t="15 April 2019 hour 10:12:30"
result= datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
result= result.year

birthday = datetime(1983,5,9,12,30,10) 

result= datetime.timestamp(birthday) #saniye
result= datetime.fromtimestamp(result) #saniye to datetime
result= datetime.fromtimestamp(0) # 1970 den bu zamana olduğunu anlamak için


result = simdi -birthday #timeelta
# result= result.days
# result= result.seconds
# result= result.microseconds

# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730,minutes=10)
result = simdi - timedelta(days=10)




print(result)
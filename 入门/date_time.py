import datetime
day = datetime.datetime.now()
ddelay = datetime.timedelta(days=1)
wdelay = datetime.timedelta(weeks = 5)
ydelay = datetime.timedelta(weeks = 56)

print(day)
print(day - ddelay)  # 一天前的时间
print(day + ddelay)  # 一天后的时间
print(day - wdelay)  # 5 周前
print(day + wdelay)  # 5 周后
print(day - ydelay)  # 一年前
print(day + ydelay)  # 一年后

print('datetime.max:' , datetime.datetime.max)
print('datetime.min:' , datetime.datetime.min)
print('datetime.resolution:' , datetime.datetime.resolution)
print('today():' , datetime.datetime.today())
print('now():' , datetime.datetime.now())
print('utcnow():' , datetime.datetime.utcnow())
print(day.strftime('%Y-%m-%d-%H:%M:%S-%f'))
print(len(day.strftime('%Y-%m-%d-%H:%M:%S-%f')))

a = 1234567890
print(len(str(a)))

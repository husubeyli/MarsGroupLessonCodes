import datetime

date = input('Date daxil edin: ')

print(date)

print(type(date))

d = datetime.datetime.strptime(date, '%Y-%m-%d')

print(d)
print(type(d))

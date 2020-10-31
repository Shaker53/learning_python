import datetime
date = input().split(' ')
year = int(date[0])
month = int(date[1])
day = int(date[2])

date_ready = datetime.date(year, month, day)

days = int(input())
days_ready = datetime.timedelta(days)

ans_date = str(date_ready + days_ready).split('-')
print(int(ans_date[0]), int(ans_date[1]), int(ans_date[2]))

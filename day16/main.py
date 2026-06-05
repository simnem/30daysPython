import datetime
today = datetime.datetime.now()

day = today.day
month = today.month
year = today.year
hour = today.hour
minute = today.minute
timestamp = today.timestamp()

print(f"Today is {day} {month} {year}, and it's exactly {hour} hours and {minute} minutes, or {timestamp}")

day_format = today.strftime("%m/%d/%Y, %H:%M:%S")

print(f"{day_format}")

todays_date = '5 December, 2019'
todays_date_formatted = datetime.datetime(todays_date, "%d %B, %Y")

print(todays_date_formatted)

date_diff = datetime.date(2027, 1,1) - datetime.datetime.now().date()
print(date_diff)


since70s = datetime.datetime.now().date() - datetime.date(1970, 1, 1)
print(since70s)
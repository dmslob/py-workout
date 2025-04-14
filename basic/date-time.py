from datetime import date

now = date.today()
print(now)

# 04-14-25. 14 Apr 2025 is a Monday on the 14 day of April
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(1983, 1, 1)
age = now - birthday
print(age.days)

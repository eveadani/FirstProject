import random
import datetime

today = datetime.datetime.today()
current_month = today.month
current_year = today.year

random_month = random.randint(1, 12)
random_year = random.randint(1980, current_year)

year_difference = current_year - random_year

if current_month >= random_month:
    month_difference = current_month - random_month
else:
    month_difference = 12 - random_month + current_month
    year_difference = year_difference-1

print(month_difference, "/", year_difference)

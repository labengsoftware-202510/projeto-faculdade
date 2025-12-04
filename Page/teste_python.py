from datetime import date
from dateutil.relativedelta import relativedelta

today = date.today()
eighth_year = today + relativedelta(years=+8)

print (today)
print (eighth_year)
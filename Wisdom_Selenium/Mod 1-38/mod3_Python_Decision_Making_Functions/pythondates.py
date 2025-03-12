from datetime import datetime

current_date = datetime.now()
print(current_date)
print(type(current_date))

formattedDate = current_date.strftime("%Y,%d %b")
print(formattedDate)
date = "28/09/2020"
string_formattedDate = datetime.strptime(date, "%d/%m/%Y")
print(string_formattedDate)

year = string_formattedDate.year
print(year)

date = string_formattedDate.day
print(date)

month = string_formattedDate.strftime("%B")
print(month)

desired_date = str(year) + "," + str(date) + " " + month
print(desired_date)

# OP:
# 2025-02-17 14:17:42.242804
# <class 'datetime.datetime'>
# 2025,17 Feb
# 2020-09-28 00:00:00
# 2020
# 28
# September
# 2020,28 September

from datetime import date, datetime, timedelta
import csv

today = date.today()
print("Today's date:", today)
d1 = date(2022, 6, 1)
d2 = date(2022, 6, 30)

delta = d2 - d1
list_of_dates = []
fieldnames = ['Date', 'Day', 'Total_hours', 'Particular']
for i in range(delta.days + 1):
    a = d1 + timedelta(days=i)
    print(a)
    b = a.strftime('%A')
    print(b)
    rows = {'Date': a,
            'Day': b,
            'Total_hours': 9,
            'Particular': 'Python'}
    list_of_dates.append(rows)

with open('/home/my/Downloads/countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list_of_dates)

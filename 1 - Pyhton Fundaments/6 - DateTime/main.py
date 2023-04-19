from datetime import date

today = date.today()
print(today)

day = date.today().day
month = date.today().month
year = date.today().year

print(day, month, year)

date_pt_br = '0{}/0{}/{}'.format( day, month, year)

print(date_pt_br)

date_br_correct = today.strftime('%d/%m/%Y')

print(date_br_correct)
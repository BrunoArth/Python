from datetime import datetime

string = '01/01/2001 00:00'

date = datetime.strptime(string, "%d/%m/%Y %H:%M")

print(date)
list_number = []
list_cumulative = []
first = True
while True:
    number = int(input("Enter a number(enter '0' to stop): "))
    if(number == 0):
        break
    list_number.append(number)
    if(first):
        list_cumulative.append(number)
        first = False
    else:
        list_cumulative.append(number+list_cumulative[-1])
print(list_cumulative)


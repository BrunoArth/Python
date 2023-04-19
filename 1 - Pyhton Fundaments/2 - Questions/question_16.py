def addition(list):
    return sum(list)
def amount(list):
    return len(list)
def media(list):
    return addition(list) / amount(list)
def receiveList():
    list = []
    while True:
        number = int(input("Enter a number(enter '0' to stop): "))
        if(number == 0):
            break
        list.append(number)
    return list

print(media(receiveList()))
def receiveList():
    list = []
    list_square = []
    list_cub = []
    while True:
        number = int(input("Enter a number(enter '0' to stop): "))
        if(number == 0):
            break
        list.append(number)
        list_square.append(number**2)
        list_cub.append(number**3)
    return list, list_square, list_cub
print(receiveList())
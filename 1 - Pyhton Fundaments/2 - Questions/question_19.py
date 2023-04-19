def receiveList():
    list = []
    while True:
        number = int(input("Enter a number(enter '0' to stop): "))
        if(number == 0):
            break
        list.append(number)
    return list
def createDic(list):
    return {
        'list': list,
        'sum':sum(list),
        'len':len(list),
        'max':max(list),
        'min':min(list)
    }
print(createDic(receiveList()))
def receiveList():
    list = []
    while True:
        number = int(input("Enter a number(enter '0' to stop): "))
        if(number == 0):
            break
        list.append(number)
    return list
def order(list):
    return sorted(list)
def amount(list):
    return len(list)

def median(list):
    list = order(list)
    n = amount(list)
    x = n//2
    if(n%2 == 0):
        return (list[x]+list[x-1])/2
    
    return list[x]

print(median(receiveList()))
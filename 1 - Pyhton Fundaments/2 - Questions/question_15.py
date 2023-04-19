list_number = []
list_new = []
while True:
    number = int(input("Enter a number(enter '0' to stop): "))
    if(number == 0):
        break
    list_number.append(number)

index = 0
indexTemp = 0
for n in list_number:
    for x in list_number:
        if(indexTemp > index):
            print(indexTemp, index)
            print(n,x)
            list_new.append([n,x])
        indexTemp +=1
    indexTemp = 0
    index +=1

print(list_new)


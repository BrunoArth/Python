import math

def receiveList():
    list = []
    while True:
        number = int(input("Enter a number(enter '0' to stop): "))
        if(number == 0):
            break
        list.append(number)
    return list
def amplitude(list):
    return max(list) - min(list)
def media(list):
    return sum(list)/len(list)
def variance(list):
    sum = 0
    for l in list:
        sum += (l+media(list))**2
    return sum/len(list)
def standard_deviation(list):
    return math.sqrt(variance(list))
def CoefficientVariation(list):
    return (100*standard_deviation(list))/media(list)

list = receiveList()
print(f"Amplitude: {amplitude(list)}")
print(f"Variance: {variance(list)}")
print(f"Standard Deviation: {standard_deviation(list)}")
print(f"Coefficient of Variation: {CoefficientVariation(list)}")

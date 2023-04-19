number = int(input("Enter a integer number: "))

list = [1,2,3,4,5,6,7,8,9,10]

print(f"number {number} table")
for n in list:
    print(f"-- {number} x {n} = {number*n} --")
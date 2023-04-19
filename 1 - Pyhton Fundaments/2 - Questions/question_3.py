area = input("Enter the area to be painted: ")
area = int(area)
print("For every liter of paint, 3 square meters are painted.")
print("Each can of paint costs $80.00 and holds 18 liters.")

quantity = area / 3
leftover = quantity
quantity = round( quantity / 18 +0.5)  
leftover = round(quantity*18 - leftover, 2)
value = quantity * 80

print(f"for an area of {area} meters {quantity} cans of paint must be purchased, which will cost ${value}. {leftover} liters of paint left.")
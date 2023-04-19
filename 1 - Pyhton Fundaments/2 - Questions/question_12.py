number = float(input("Enter a number: "))

decimal = round(number - (round(number -0.5)), 2)
decimal = int(round(decimal*100,2))

if decimal == 1: 
    decimal = 0

print(f"Decimal the {number} is: {decimal}")
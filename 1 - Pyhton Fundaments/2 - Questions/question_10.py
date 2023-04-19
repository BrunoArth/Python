first_number = int(input("First number: "))
txt = "First number"
bigger = first_number
second_number = int(input("Second number: "))
if second_number>bigger:
    bigger = second_number
    txt = "Second number"
third_number = float(input("Third number: "))
if third_number>bigger:
    bigger = third_number
    txt = "Third number"
fourth_number = float(input("Fourth number: "))
if fourth_number>bigger:
    bigger = fourth_number
    txt = "Fourth number"
fifth_number = float(input("Fifth number: "))
if fifth_number>bigger:
    bigger = fifth_number
    txt = "Fifth number"

print(f"{txt}: {bigger}")
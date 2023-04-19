first_product = int(input("First Product: "))
txt = "First product"
smaller = first_product
second_product = int(input("Second Product: "))
if second_product<smaller:
    smaller = second_product
    txt = "Second product"
third_product = float(input("Third Product: "))
if third_product<smaller:
    smaller = third_product
    txt = "Third product"

print(f"{txt}: ${smaller}")
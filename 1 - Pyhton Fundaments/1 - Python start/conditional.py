b = True
if b:
    print("Is True")
n = input("enter a number between 0 and 10:  ")
n = int(n)

if n >= 0 and n <= 10:
    print("OK")
else:
    print("Invalid!")

if n==0:
    print("n = 0")
elif n >= 1 and n < 5:
    print("0 < n > 5")
elif n == 5:
    print("n = 5")
elif n>5 and n<10:
    print("6 < n > 10")
elif n == 10:
    print("n = 10")
else:
    print("Invalid!")

a = int(input("how old are you: "))
if a >= 16:
    print("you are already of legal age!")
else:
    print("you are not of legal age!")
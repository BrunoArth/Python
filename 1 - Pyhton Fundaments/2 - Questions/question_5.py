score_test_1 = float(input("Test Score 1: "))
score_test_2 = float(input("Test Score 2: "))
media = (score_test_1+score_test_2)/2 
if media <7 and media>=0:
    print("Failed")
elif media==10:
    print("Passed with distinction")
elif media >=7 and media <10:
    print("Passed")
else:
    print("Invalid")

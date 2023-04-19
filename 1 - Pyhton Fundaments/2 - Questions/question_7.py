string = str(input("Type e string: "))

if 'a' in string or 'A' in string:
    print(f"The string has {string.count('a')+string.count('A')} vowels 'a'")
if 'e' in string or 'E' in string:
    print(f"The string has {string.count('e')+string.count('E')} vowels 'e'")
if 'i' in string or 'I' in string:
    print(f"The string has {string.count('i')+string.count('I')} vowels 'i'")    
if 'o' in string or 'O' in string:
    print(f"The string has {string.count('o')+string.count('O')} vowels 'o'")
if 'u' in string or 'U' in string:
    print(f"The string has {string.count('u')+string.count('U')} vowels 'u'")
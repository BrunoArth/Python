information = {'name': 'Maria', 'old': 23}

print(f'.keys(): {information.keys()}')
print(f'.valuers():{information.values()}')

information['height'] = 1.60
print(f'add vale: {information}')

information.pop('name')
print(f'.pop(name): {information}')

information.popitem()
print(f'.popitem(): {information}')

hobbies = {'read': ['Start Python 3', 'Fundaments of pyhton'], 'watch': ['movies', 'soccer','series','anime','memes','reality shows']}
information.update(hobbies)
print(f'.update(): {information}')

# WTF!!! :(
LETTER_NUMBER = [
    ('a', 1),
    ('b', 2),
    ('c', 3),
    ('d', 4),
    ('e', 5)
]

letter_number = {number: letter for letter, number in LETTER_NUMBER} #WTF!!!!!!!!!!!!!!! :(
print(letter_number)
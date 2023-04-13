word = []
loop = True
while(loop):
    word.append(input("type a letter: "))
    x = input("continue or type 'exit' to stop: ")
    if(x == 'exit'):
        loop = False
    for i in range(0, len(word)):
        print(f"{i+1} - {word[i]} ")
for i in range(0, len(word)):
    print(f"{i+1} - {word[i]} ")


old_friend = [["Bru", 16], ["Bel", 15], ["Xan", 17], ["Els", 19]]

for f in old_friend:
    print(f'Name: {f[0]}')
    print(f'Old: {f[1]}')
    
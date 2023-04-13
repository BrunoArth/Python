int_list_example = [1,2,3,4]
dinamic_list = [1, "text", True, 2.9]
empty_list = []

print(int_list_example)
print(dinamic_list[0])
print(dinamic_list[1])
print(dinamic_list[-1])
print(dinamic_list[-2])
print(dinamic_list[1:3])
print(dinamic_list[0:1])
print(dinamic_list[0:2])
print(dinamic_list[1:])
print(dinamic_list[-3:])

dinamic_list[2] = 3
print(dinamic_list[2])
dinamic_list[2] = False
print(dinamic_list)

list_a = [11,2,33,41,0.5]
list_b = list_a
list_c = list_a[:]

list_b[1] = 3

print(list_a)
print(list_b)

list_a[2] = "20"

print(list_a)
print(list_b)

print(list_c)

list_c.append(10)
print(list_c)

list_c.pop(0)
print(list_c)

list_c.sort()
print(list_c)

list_c.sort(reverse=True)
print(list_c)

print(len(list_c))

list_c.insert(10, 2)
print(list_c)

list_c.reverse()
print(list_c)


print(list_c.count(2))


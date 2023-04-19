list = [0,0,1,2,3,4,5,0,0,1]
s = sum(list)
q = len(list)

valids = [l for l in list if l > 0]
print(valids)

valids = sum([3.0<=l<=5.0 for l in list])
print(valids)
tup = (1,2,3,4,5,7,8)

tup = list(tup)
tup.remove(3)
tup.remove(4)
tup = tuple(tup)
print(len(tup))
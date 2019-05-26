

lst = [2, 3, 4, 5]
lst2 = lst
lst2.append(20)
print(lst2)
print(lst)

a = 10
b = a
b = 20
print(a)
lst3 = lst2[:] #start an ending point
print(lst3)
lst3.append(45)
print(lst3)
print(lst2)
print(lst2[4::-1]) #reverse line/ step size

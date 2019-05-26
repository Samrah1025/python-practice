#n = int(input("Enter a number")
#arr = []
#for _ in range(1,100):
 #   x = int(input())
  #  arr.append(x)    

import random
lst = []
for i in range(0, 10):
     lst.append(random.randint(1, 1000))
print(lst) 
min_val = lst[0]
min_idx = 0
for i in range(1, len(lst)):
    if lst[i] < lst[i + 1]:
         min_val = lst[i]
         min_idx = i
print("minimum value:", min_val)     
print("minimum index:", min_idx)    
      

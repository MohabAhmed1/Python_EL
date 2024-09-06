lst = []

no_ele = int(input("Enter the number of elements : "))

for i in range (1 , no_ele + 1 ):
    x = int(input())
    lst.append(x)

print(lst)

print ("The counts of no 4 in list = " , lst.count(4))




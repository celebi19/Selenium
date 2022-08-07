
""" tuple1 = (10,20,30,40)
print(tuple1)
count = 0
for i in tuple1:
    print("tuple1[%d] = %d" %(count,i))




tuple1 = (10,20,30,40)
print(tuple1)
xcount = 0
for i in tuple1:
    print("tuple1[%d] = %d" %(xcount,i))


# exmaple 2

tuple1 = tuple(input("Enter the tuple elements..."))
print(tuple1)
count=0
for i in tuple1:
    print("tuple1[%d]= %s" %(count,i))

"""

#example 3
t3 =()
print(t3) #prints ()

t4 =(90,)
print(t4)

#example 4

tuple1 = (1,2,3,4,5)
print(tuple1[-1]) # prints 5
print(tuple1[-4]) # prints 2
print(tuple1[0:]) # prints (1, 2, 3, 4, 5)

print(tuple1[0:6]) # prints (1, 2, 3, 4, 5)
print(tuple1[:]) # prints (1, 2, 3, 4, 5)


#example 5
tuple5 = [(101, "John", 22), (102, "Mike", 28),  (103, "Dustin", 30)]
print(tuple5)
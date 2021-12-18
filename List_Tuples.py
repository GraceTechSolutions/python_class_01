# l1 = ['Hello', 2.5, 199, 7j, False, 2.0]
# l2 = ['Data from list 2', 'Another Data from list 2']

# Indexing & Slicing
    # list1[2]
    # list1[0:3] Same as list1[:3]
    # list1[1:5:2] # Here 2 is step size


# Create a list using range
    #  Range generates a seq of int which can be stored in a list
# r = range(0, 10)
# my_list = list(r)

# CRUD
# create read update delete
# l = [1,2,3,4]
# l[n]

# Update
# list1
# list1.append(element) # Append element at the end
# list1[0] = 'Hii'

# Delete
# list1
# del list1[0]
# del list1[0:3]
# del list1
# list1.remove(2) # Delete first '2'

# Other methods
# list1.reverse()

# Membership

# l1 = ['Hello', 2.5, 199, 7j, False, 2.0]
# x = 19

# print(x in l1)

# Cloning
# l3 = l1
# l1[0] = 'Hii'
# print(l3)

# list1 = [1,2,3,4,5,2,6,8,2,9]
# n = list1.copy()
# list1[0] = 100

# print(n)
# print(list1)

# list1.extend([9,8,7,6])

# print(list1)

# p = list1.count(2)
# print(p)

# r = list1.pop()

# print(r)
# print(list1)

list1 = [1,2,3,4,5,0,2,6,80,2,-9]

# r = list1.sort() 
# print(r) # print None
# print(list1)

# list1.clear()
# print(list1)

# data = sum(list1)
# print(data)

# print(max(list1))
# print(min(list1))


# list1.sort(reverse=True)
# print(list1)

# Nested list as matrix
# [1 2 3 4 5]
# [6 7 8 9 0]
# [0 9 8 7 6]
# [5 4 3 2 1]

# Nested list
# e1 = 'Hello'
# e2 = 1
e3 = [5, 6, 7, 8]

# list_main = [e1, e2, e3]
# print(list_main)

# Matrix
# e1 = [1,2,3]
# e2 = [4,5,6]
# e3 = [7,8,9]

# matrix = [e1, e2, e3]



# Tuples
# t = (1, 2, 3, 4, 5)
# t2  = tuple(e3)

# print(type(t2))
# res = tuple(sorted(t, reverse=True))
# print(res)


# Nested tuple
# t = (1,2,3,4, (7,8,9))
# print(t[4][0])

# emp = (
#     (10, 'Jay', 1991),
#     (4, 'Raj', 1994),
#     (7, 'Neha', 1992),
#     (6, 'Mohan', 1989)
# )

# res = sorted(emp, reverse=True) #Sort by work exp
# res = sorted(emp, key=lambda x: x[1]) #Sort by name
# res = sorted(emp, key=lambda x: x[2]) #Sort by dob

# print(res)

# Inserting element in tuple
# t = (1,2,3,4,5)
# pos = 3
# element = 9

# y = t[:pos-1]
# y += (element,)
# t = y + t[pos-1:]

# print(t)

# Delete
# t = (1,2,3,4,5)
# pos = 3
# print(t)

# y = t[:pos-1]
# t = y + t[pos:]

# print(t)


# Update
# t = (1,2,3,4,5)
# pos = 3
# element = 8

# print(t)

# y = t[:pos-1]
# y += (element,)
# t = y + t[pos:]

# print(t)

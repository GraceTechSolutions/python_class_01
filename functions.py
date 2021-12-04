# def function_name(arguments):
#     """Doc String"""
#     statements

# Basic function with two arguments
# def sum(x, y):
#     print(x + y)


# Function with two args and their type
# def sum(x:int, y:int):
#     """Takes two int variables and print their sum"""
#     print(x + y)

# Returning value from function

# Returning single argument
# def sum(x: int, y: int):
# """Takes two int variables and return their sum"""
#     z = x + y
#     return z

# res = sum(6,9)

# Returning multiple argument
# def sum(x: list, y: list):
#     """Takes two list and print return sum"""
#     res1 = 0
#     res2 = 0
#     for i in x:
#         res1 += i
    
#     for i in y:
#         res2 += i

#     return res1, res2

# x, y = sum([2,4,7,1], [6,9,7,5])
# print(type(x))
# print(x)

# print()

# print(type(y))
# print(y)



# Assigning function to a variable
# def sum(x:int, y:int):
#     """Takes two int variables and print their sum"""
#     print(x + y)
#
# copy_of_sum = sum
# copy_of_sum(2,5)

# Function arguments
# 1. Postioonal args
# 2. Keyword args
# 3. Default args
# 4. Variable length args

def sub(first_number:int, second_number:int):
    return first_number - second_number

# Postioonal args
# res = sub(x, y)
# print(res)


# Keyword args
# res = sub(second_number=5, first_number=10)
# print(res)

# Default args
# def greet(name='User', age=20):
#     print('Hello {}\nYou are {}'.format(name, age))

# greet(age=23)
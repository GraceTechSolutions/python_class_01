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

# def sub(first_number:int, second_number:int):
#     return first_number - second_number

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

# Variable length args [0]
# def sum(f_number: int, *args):
#     res = f_number
#     for num in args:
#         res += num
#     print(res)

# sum(2, 4, 1, 3)

# Variable length args [1]
# def print_all(f_number: int, **kwargs):
#     print(f'Your first number is {f_number}')
#     print(kwargs)

# print_all(10, name='Jay', age=23, home='Mumbai')


# Local and global variables
# var1 = 100

# def create_var(x):
#     global var1
#     var1 = x
#     print(var1)

# create_var(20)
# print(var1)


# Recursive functions
# def factorial(n):
#     if n == 0:
#         result = 1
#     else:
#          result = n*factorial(n-1)
    
#     return result

# res = factorial(4)
# print(res)

# Anonymous functions or Lambdas
# def square(n):
#     return n*n

# sq = lambda n: n*n

# print(sq(5))


# Filter
#
# def check_even(y):
#     return y%2 == 0
# 
# l = [1,2,3,4,5,6,7,8,9]
# res = filter(lambda y: y%2==0, l)
# print(list(res))
# print(res)
# print(type(res))


# Map
# def add_10(n):
#     return n + 10
# 
# l = [1,2,3,4,5,6,7,8,9]
# res = map(lambda n: n + 10, l)
# print(res)
# print(list(res))


# Reduce
# from functools import reduce
# def add_all(x, y):
#     print(f'First is {x} & second is {y}')
#     return x + y
# 
# l = [1,2,3,4]
# res = reduce(add_all, l)
# print(res)
# print(type(res))



# Decorators

# def sub(x, y):
#     print(x-y)

# def div(x, y):
#     print(x/y)


# def smart(func):
#     def main(a, b):
#         if a < b:
#             a,b = b,a
#         return func(a, b)
    
#     return main

# s_sub = smart(sub)
# s_div = smart(div)

# valx = 3
# valy = 6

# sub(valx, valy)
# s_sub(valx, valy)

# div(valx, valy)
# s_div(valx, valy)



# Function Decorators
# def print_all(func):

#     def main():
#         print('I am from print_all function')
#         return func()
    
#     return main


# @print_all
# def greet():
#     print('Good morning..')

# greet()



# def smart(func):
#     def main(a, b):
#         if a < b:
#             a,b = b,a
#         return func(a, b)
    
#     return main

# @smart
# def div(x, y):
#     print(x/y)


# div(2, 8)





#(not) Generators
# Find first 10 even numbers
# def find():
#     n = 1
#     i = 1
#     ret_list = []
#     while True:
#         num = n%2
#         if num == 0:
#             ret_list.append(n)
#             i+=1
        
#         n += 1
#         if i > 10:
#             break
#     return ret_list

# print(find())

# ret_list --


# Generators
# def find():
#     n = 1
#     i = 1
#     while True:
#         num = n%2
#         if num == 0:
#             yield n
#             i+=1
        
#         n += 1
#         if i > 10:
#             break

# ret_value -----------

# Modules & main function
# from modules import print_main as pm1
# from day9 import print_main as pm2

# pm1()
# pm2()
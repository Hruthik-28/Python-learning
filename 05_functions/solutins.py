# def square_of_num(number):
#     return number ** 2

# result = square_of_num(2)

# print(result)


# def sum_of_num(num1, num2):
#     return num1 + num2

# result = sum_of_num(2, 3)
# print(result)


# def multiply(first, second):
#     return first * second

# print(multiply(8, 5))
# print(multiply("hruthik", 5))
# print(multiply(5, "hruthik"))

# import math

# def circle_stats(radius):
#     area = round(math.pi * radius ** 2, 2)
#     circumference = round(2 * math.pi * radius, 2)
#     return area, circumference

# area, circumference = circle_stats(5)
# print("Area: ", area, "circumference: ", circumference)

# def greet(name = "alex"):
#     return "Hello, " + name + "!"

# print(greet("Hruthik"))


# cube = lambda x: x ** 3
# print(cube(2))


# def sum_all(*args):
#     return sum(args)

# print(sum_all(1, 1))
# print(sum_all(1, 1, 2))


# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
    
# print_kwargs(name="Gojo", power="Red")
# print_kwargs(name="Gojo", power="Red", enemy="Sukuna")
# print_kwargs(name="Itadori")


# def generate_even_num(limit):
#     for i in range(2, limit+1, 2):
#             yield i

# for num in generate_even_num(10):
#     print(num)

# yield returns the value but also keeps the function in the memory and its state

# def factorial(number):
#     if number == 0:
#         return 1
#     else: 
#         return number * factorial(number - 1)

# print(factorial(5))
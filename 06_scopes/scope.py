
# def func():
#     username = "chai"
#     print(username)

# func()


# x = 99

# def func2(y):
#     z = x + y
#     return z

# print(func2(1))

# x = 99

# def func3():
#     global x
#     x = 12

# func3()
# print(x)


# x = 99

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2

# result = f1()
# result()

def chaiCoder(num):
    def actual(x):
        return x ** num
    return actual
    
    
coder1 = chaiCoder(3)
print(coder1(2))

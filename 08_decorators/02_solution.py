def debug_function_call(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}:{v}"for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args: {args_value} and kwargs: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug_function_call
def test_function(name, age, phone):
    return f"My name is {name}, {age} years old, and my phone is {phone}"

test_function("Hruthik", 21, phone=555888333)
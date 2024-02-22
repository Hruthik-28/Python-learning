def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Gojo", power="Red")  # Output: name: Gojo, power: Red
print_kwargs(name="Gojo", power="Red", enemy="Sukuna")  # Output: name: Gojo, power: Red, enemy: Sukuna
print_kwargs(name="Itadori")  # Output: name: Itadori

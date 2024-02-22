def generate_even_num(limit):
    for i in range(2, limit+1, 2):
            yield i

for num in generate_even_num(10):
    print(num)  # Output: 2, 4, 6, 8, 10

number = 10

for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(number, 'x', i, "=", number * i)

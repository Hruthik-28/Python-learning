order_size = "large"
extra_shot = False

if extra_shot:
    coffee = order_size + "coffee with an espresso"
else:
    coffee = order_size + "coffee"

print(coffee)
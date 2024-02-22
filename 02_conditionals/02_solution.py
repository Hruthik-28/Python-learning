age = 21
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

price("Your Ticket Price is:", price)
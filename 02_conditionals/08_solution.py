password = "secure@5"
password_length = len(password)

if password_length < 6:
    print("weak password")
elif password_length <= 10:
    print("Medium password")
else: 
    print("Strong Password")
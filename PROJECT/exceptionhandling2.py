try:
    username = input ("username: ")
    password = input ("password: ")
    if password != "admin123":
        raise ValueError("incorrect password")
    print("Login succesful")
except ValueError as e:
    print(e)
try:
    a=10
    b=2
    print(a/b)
except ZeroDivisionError:
    print("Error")
else:
    print("Execution successful")
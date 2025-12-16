def welcome():
    print("Welcome to Python Functions")

def add(a, b):
    print("Addition:", a + b)

def get_number():
    return 10

def square(n):
    return n * n

def show_length(text):
    print("Length of text:", len(text))

multiply = lambda x, y: x * y

welcome()

add(5, 3)

num = get_number()
print("Number:", num)

print("Square:", square(4))

show_length("Python")

print("Multiply:", multiply(2, 5))
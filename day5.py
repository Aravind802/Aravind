n = int(input("Enter a positive integer: "))

for i in range(1, n+1):
    print(i)

sum_numbers = 0
i = 1
while i <= n:
    sum_numbers += i
    i += 1

print("Sum of numbers:", sum_numbers)
def calculate_square(n):
    return n * n

n = int(input("Enter a positive integer: "))
result = calculate_square(n)
print("Square of", n, "is", result)

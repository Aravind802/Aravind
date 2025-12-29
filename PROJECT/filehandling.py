# Create and write to example.txt
with open("example.txt", "w") as f:
    f.write("Python file handling\n")

# Append data to example.txt
with open("example.txt", "a") as f:
    f.write("Easy and Powerful\n")

# Read from example.txt
with open("example.txt", "r") as f:
    print(f.read())


# Create and write to student.txt
file = open("student.txt", "w")
file.write("Name: Aravind\n")
file.close()

# Append data to student.txt
file = open("student.txt", "a")
file.write("Grade: A\n")
file.close()

print("Data appended")
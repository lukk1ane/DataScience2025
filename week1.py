# Task 1: Basic Variables and Printing 
age = 25
name = "Nini"
print(age) 
print(name)

# Task 2: Type Conversion
length = 10.5
int_length = int(length)
print(type(length))
print(type(int_length))

# Task 3: Formatted Printing
x = 5
y = 10.5
z = "Hello"
print(f"x: {x}, y: {y}, z: {z}")

# Task 4: Simple Function 
def greet(name):
    return f"Hello, {name}!"

print(greet("Nini"))

# Task 5: Conditional Statements 
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print(is_even(4))
print(is_even(7))

# Task 6: Lists and Dictionaries
fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}

for fruit in fruits:
    print(f"{fruit} is {fruit_colors[fruit]}")


# Task 7: List Comprehension
squares = [x**2 for x in range(1,11)]
print(squares)

# Task 8: For Loop with Conditional
for i in range(1,21):
    if i % 3 == 0:
        print(i)

# Task 9: Function with Loop and Conditionals 
def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(20)

# Task 10: Error Handling - Division
def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
print(division(20, 2))
print(division(5, 0))
print(division(5, 2))

# Task 11: Error Handling - List Index 
def list_index(lst, i):
    try:
        return lst[i]
    except IndexError:
        return "Index out of range"

numbers = [1, 2, 3, 4, 5]
print(list_index(numbers, 3))
print(list_index(numbers, 5))

# Task 12: User Input and Error Handling 
while True:
    try:
       user_input = int(input("Enter a number: "))
       print(f"The square of {user_input} is {user_input ** 2}")
       break 
    except ValueError:
        print("Invalid input.")


# Task 13: File Writing
with open("hello.txt", "w") as f:
    f.write("Hello, World!")
print("Wrote successfully")

# Task 14: File Reading
try:
    with open("hello.txt", "r") as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError:
    print("File does not exist.")

# Task 15: File Processing 
with open("numbers.txt", "w") as f:
    f.write("1\n2\n3\n4\n5")

try:
    with open("numbers.txt", "r") as f:
        numbers = f.readlines()

    numbers = [int(x.strip()) for x in numbers]  
    total = sum(numbers)
    average = total / len(numbers)

    print("Sum:", total)
    print("Average:", average)
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("File contains non-numeric data.")
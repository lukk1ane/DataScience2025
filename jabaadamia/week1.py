# Task 1: Basic Variables and Printing
age = 25
name = "jaba"

print(f'{name} {age}')

# Task 2: Type Conversion
length = 10.5
int_length = int(length)

print(f'{type(length)} {type(int_length)}')

# Task 3: Formatted Printing
x = 5
y = 10.5
z = "Hello"

print(f'x: {x}, y: {y}, z: {z}')

# Task 4: Simple Function
def greet(name):
    return f'hello {name}'

print(greet("jaba"))

# Task 5: Conditional Statements
def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))


# Task 6: Lists and Dictionaries
fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}

for fruit in fruits:
    print(f'{fruit} - {fruit_colors.get(fruit)}')

# Task 7: List Comprehension
squares = [i*i for i in range(1,10)]
print(squares)

# Task 8: For Loop with Conditional
for i in range(1, 20):
    if i % 3 == 0:
        print(i)

# Task 9: Function with Loop and Conditionals
def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(20)

# Task 10: Error Handling - Division
def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("cant divide by 0")

div(13, 2)
div(15, 0)

# Task 12: User Input and Error Handling
try:
    a = int(input("enter integer: "))
    print(a*a)
except ValueError:
    print("type of input should be int!")

# Task 13: File Writing
with open("hello.txt", "w") as file:
    file.write("Hello, World!")

print("Text written successfully to hello.txt")

# Task 14: File Reading
try:
    with open("hello.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: 'hello.txt' does not exist")

# Task 15: File Processing
try:
    numbers = []
    with open("numbers.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    numbers.append(int(line))
                except ValueError:
                    print(f"non-numeric data: {line}")
    
    total = sum(numbers)
    average = total / len(numbers)
    print(f"sum: {total}")
    print(f"average: {average}")

except FileNotFoundError:
    print("numbers.txt does not exist.")
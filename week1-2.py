# Python Practice - Learning the Basics
# Just working through some exercises to get better at Python!

# ============================================
# Task 1 - Getting started with variables
# ============================================
age = 25
name = "anano"
print(age)
print(name)

# ============================================
# Task 2 - Converting between types
# ============================================
length = 10.5
int_length = int(length)  # this cuts off the decimal part
print(type(length))
print(type(int_length))

# ============================================
# Task 3 - Printing multiple things at once
# ============================================
x = 5
y = 10.5
z = "Hello"
print(f"x: {x}, y: {y}, z: {z}")

# ============================================
# Task 4 - My first function!
# ============================================
def greet(name):
    return f"Hello, {name}! Welcome!"

print(greet("Anano"))

# ============================================
# Task 5 - Checking if numbers are even
# ============================================
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # should be True
print(is_even(7))  # should be False

# ============================================
# Task 6 - Working with lists and dictionaries
# ============================================
fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}

# let's match each fruit with its color
for fruit in fruits:
    print(f"{fruit}: {fruit_colors[fruit]}")

# ============================================
# Task 7 - List comprehension (fancy one-liner!)
# ============================================
squares = [num ** 2 for num in range(1, 11)]
print(squares)

# ============================================
# Task 8 - Finding numbers divisible by 3
# ============================================
for num in range(1, 21):
    if num % 3 == 0:
        print(num)

# ============================================
# Task 9 - The classic FizzBuzz problem
# ============================================
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:  # divisible by both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(20)

# ============================================
# Task 10 - Handling division by zero
# ============================================
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Oops! Can't divide by zero"

print(divide(10, 2))
print(divide(10, 0))  # this will trigger the error handling

# ============================================
# Task 11 - Dealing with invalid list indexes
# ============================================
def get_list_value(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "That index doesn't exist!"

my_list = [10, 20, 30, 40, 50]
print(get_list_value(my_list, 2))  
print(get_list_value(my_list, 10))  

# ============================================
# Task 12 - Getting input from the user
# ============================================
def get_square_input():
    while True:
        try:
            num = int(input("Give me a number: "))
            print(f"The square is {num ** 2}")
            break
        except ValueError:
            print("That's not a number! Try again.")



# ============================================
# Task 13 - Writing to a file
# ============================================

with open('hello.txt', 'w') as f:
    f.write("Hello, World!")
print("File created successfully!")

# ============================================
# Task 14 - Reading from a file
# ============================================
try:
    with open('hello.txt', 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Hmm, couldn't find that file...")

# ============================================
# Task 15 - Processing numbers from a file
# ============================================

# First, let's create a file with some numbers
with open('numbers.txt', 'w') as f:
    f.write("10\n20\n30\n40\n50\n")

# Now let's read it and calculate sum and average
try:
    with open('numbers.txt', 'r') as f:
        numbers = []
        for line in f:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                print(f"Skipping '{line.strip()}' - not a number")
        
        if numbers:
            total = sum(numbers)
            avg = total / len(numbers)
            print(f"Sum: {total}")
            print(f"Average: {avg}")
        else:
            print("No valid numbers found")
            
except FileNotFoundError:
    print("File not found!")

print("\nAll done!")
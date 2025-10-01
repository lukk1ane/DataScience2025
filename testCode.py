from numpy.ma.extras import average

age = 25
name: str = "Jumber"
print(age)
print(name)

length = 10.5
int_length = int(length)
print(type(length))
print(type(int_length))

x = 5
y = 10.5
z =  "Hello"
print(f"x: {x}, y: {y}, z: {z}")

def greet(name):
    print(f"Hello, {name}")

greet("Jumber")

def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))

fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}

for fruit in fruits:
    print(f"{fruit}: {fruit_colors[fruit]}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x ** 2 for x in numbers]
print(squares)

for i in range(1, 20):
    if i % 3 == 0:
        print(i)

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else: print(i)

fizz_buzz(20)

def div(num1, num2):
    try:
        print(num1 / num2)
    except ZeroDivisionError: print("Can't divide by zero")

div(8, 4)
div(3, 4)
div(1, 0)

def getAtIndex(list, index):
    try:
        print(list[index])
    except IndexError: print("Index out of range")

getAtIndex([1, 2, 3], 0)
getAtIndex([1, 2, 3], 2)
getAtIndex([1, 2, 3], 3)

def read():
    userInput = ""
    while type(userInput) != int:
        userInput = input("Enter the input")
        try:
            num = int(userInput)
            print(num ** 2)
            return
        except ValueError: print("Invalid input")

read()

"""
with open("hello.txt", "a") as f:
  f.write("Hello World!")
  print("Message written successfully")
"""

try:
    with open("hello.txt") as f:
      print(f.read())
except FileNotFoundError: print("File not found")

try:
    with open("numbers.txt") as f:
        numbers = [int(line.strip()) for line in f]
        sm = sum([x for x in numbers ])
        avg = average([x for x in numbers])
        print(sm)
        print(avg)
except FileNotFoundError: print("File not found")






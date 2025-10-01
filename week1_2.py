# Task 1
age = 25
name = "Beso40k"
print(age,name)

# Task 2

length = 10.5
int_length = int(length)
print(length,int_length)

# Task 3

x, y, z = (5, 10.5, "Hello")
print(f"x: {x}, y: {y}, z: {z}")

# Task 4
def greet(name):
    return f"Hello, {name}"

print(greet("beso"))

# Task 5
def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))

# Task 6
fruits  = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}
for fruit in fruits:
    print(f"{fruit} is {fruit_colors[fruit]}")

# Task 7

print([i ** 2 for i in range(1, 11)])

# Task 8

for i in range (1, 20):
    if i % 3 == 0:
        print(i)

# Task 9

def fizz_buzz(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(20)


# Task 10

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)
except ZeroDivisionError:
    print("can't divide by zero champ")
except ValueError:
    # might as well type conversion error
    print("wrong type, try again comrade")
finally:
    print("finished")

# Task 11

def find_index(list, index):
    return list[index]

try:
    a = input("Enter the list seperated by comma: ")
    a = a.split(",")
    b = int(input("Enter the index: "))
    print(find_index(a, b))
except ValueError:
    print("wrong type, try again comrade")
except IndexError:
    print("there ain`t no index like that here")

# Task 12

while True:
    try:
        n = int(input("Enter an integer: "))
        print(n**2)
        break
    except ValueError:
        print("wrong type, try again comrade")

# Task 13

with open("hello.txt", "w") as file:
    try:
        file.write("Hello World!")
        print("File created successfully")
    except FileNotFoundError:
        print("file not found")

# Task 14

try:
    with open("hello.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")

# Task 15

with open("numbers.txt", "w")as file:
    for i in range(1, 100):
        file.write(str(i))
        file.write("\n")

try:
    with open("numbers.txt", "r") as file:
        total = 0
        counter = 0
        for line in file:
            total += int(line)
            counter += 1
        print(total, total/counter)
except FileNotFoundError:
    print("file not found")
except TypeError:
    print("wrong type, try again comrade")

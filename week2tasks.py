# task 1
from logging import exception

from executing import cache

age = 25
name = "dato"

print(age, name, sep='\n')

# task 2
length = 10.5
int_length = int(length)
print(type(length), type(int_length))

# task 3
x, y, z = 5, 10.5, 'Hello'
print(f'x: {x}, y: {y}, z: {z}')

# task 4
def greet(name: str):
    print(f'Greetings, {name}')

greet("Dato")

# task 5
def is_even(num: int):
    return num % 2 == 0

print(is_even(42))
print(is_even(67))

# task 6
fruits = ['apple', 'banana', 'orange']
fruit_colors =  {"apple": "red", "banana": "yellow", "orange": "orange"}

for fruit in fruits:
    print(f'{fruit} is {fruit_colors[fruit]}')

# task 7
squares = [i**2 for i in range(1, 11)]
print(squares)

# task 8
for n in range(1, 20):
    if n % 3 == 0:
        print(n, end=' ')

print()

# task 9
def fizz_buzz(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizz_buzz(20)

# task 10
def divide(a, b):
    return a / b

try:
    print(divide(2, 3))
    print(divide(10, 0))
except ZeroDivisionError:
    print("Cannot divide by zero")

# task 11
def ith(list, index ):
    return list[index]

try:
    print(ith([1,2,3], 2))
    print(ith([1,2,3], 3))
except IndexError:
    print('index out of bounds')

# task 12
while True:
    try:
        num = int(input("Enter an integer: "))
        print(f"square is {num**2}")
        break
    except Exception:
        print("I said enter an integer, try again.")

# task 13
with open('hello.txt', 'w') as file:
    file.write("Hello, World!")
    print("Success")

# task 14
try:
    with open('hello.txt', 'r') as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f'something went wrong: {e}')

#task 15
try:
    with open('numbers.txt', 'w') as file:
        for i in range(1, 11):
            file.write(str(i) + '\n')
except Exception as e:
    print("error occured, " + e)


try:
    with open("numbers.txt", "r") as file:
        lines = file.readlines()

    numbers = []
    for line in lines:
        line = line.strip()
        if line:
            try:
                numbers.append(float(line))
            except ValueError:
                print(f"non-numeric data ignored: '{line}'")

    if numbers:
        total = sum(numbers)
        average = total / len(numbers)
        print(f"\nSum of numbers: {total}")
        print(f"Average of numbers: {average}")
    else:
        print("No valid numbers found in the file.")

except FileNotFoundError:
    print("file 'numbers.txt' does not exist.")
except Exception as e:
    print(f" error occurred: {e}")
#task 1
from warnings import catch_warnings

age=25
name="Lika"
print(age)
print(name)

#task 2
length=10.5
int_length=int(length)
print(type(length))
print(type(int_length))

#task 3


x=5
y=10.5
z='Hello'
print(f"x: "+str(x) +", y: "+ str(y) + ", z: "+ str(z))


#task 4
def greet(name):
    return "hello " + name

print(greet("lika"))

#task 5
def is_even(num):
    if num%2==0:
        return True
    else: return False
print(is_even(4))
print(is_even(7))

# task 6
fruits=["apple", "banana", "orange"]
fruit_colors= {"apple":"red", "banana": "yellow", "orange": "orange"}
for fruit in fruits:
    print(f"{fruit} {fruit_colors.get(fruit)}")

#task 7
squares = [x**2 for x in range(1,11)]
print(squares)

#task 8
for n in range(1, 21):
    if n%3==0:
        print(n)
#task 9
def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("Fizz")
        else: print(i)

fizz_buzz(20)

#task 10
def division(a, b):
    try:
       return a//b
    except ZeroDivisionError:
        print("You can’t divide by zero!")
print(division(4,2))

# task 11
def list_index(lst, i):
    try:
        lst[i]
    except IndexError:
         print("Oops! Index out of bounds.")

#task 12
number=int(input("Insert a number: "))
print(number*number)

#task 13
with open("hello.txt", "w") as f:
    f.write("Hello, World\n")
print("File created successfully!")

#task 14
try:
    with open("hello.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("The file doesn't exist")

#task 15
with open("numbers.txt", "w") as f:
    f.write("10\n20\n30\n40\n50\n")  # example numbers

print("numbers.txt created successfully!")

try:
    with open("numbers.txt", "r") as f:
        lines = f.readlines()

    numbers = []
    for line in lines:
        try:
            numbers.append(float(line.strip()))
        except ValueError:
            print(f"Skipping invalid data: {line.strip()}")

    if numbers:
        total = sum(numbers)
        average = total / len(numbers)
        print(f"Sum: {total}")
        print(f"Average: {average}")
    else:
        print("No valid numbers found in the file.")

except FileNotFoundError:
    print("Error: 'numbers.txt' does not exist.")


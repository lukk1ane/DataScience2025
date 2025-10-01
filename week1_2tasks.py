
# Task1
age = 25
name= "Tamari"
print(age)
print(name)

# Task2
length=10.5
int_length = int(length)
print(type(int_length))
print(type(length))

# Task3
(x,y,z) = (5,10.5,"Hello")
print(x,y,z)

# Task4
def greet(name):
    return f"Hello {name}"
print(greet("Tamar"))

# Task5
def is_even(n):
    return n % 2 == 0
print(is_even(4))
print(is_even(7))

# Task6
fruits= ["apple", "banana", "orange"]
fruit_colors = {"apple":"red", "banana":"yellow", "orange":"orange"}
for fruit in fruits:
    print(fruit + " " + fruit_colors[fruit])

#Task 7

numbers = range(1,11)
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

#Task 8
for i in range(1,21):
    if i % 3 == 0:
        print(i)

#Task 9
def fizz_buzz(n):
    for i in range(1,n+1): #loop runs from 1 through n
        if i%15==0:  #Least Common Multiple of 5 and 3 is 15
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        else: #rest cases
            print(i)

print(fizz_buzz(20))

#Task 10
def division(n,m):
    try:
        return n/m
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(division(2,3))
print(division(5,0))

#Task 11
def indexOfList(list, index):
    try:
        return list[index]
    except IndexError:
        return "Index out of the bound"

print(indexOfList(["apple","banana","orange"],5))

#Task 12
def task12():
    while True:
        numb = input("enter number: ")
        try:
            intnumb = int(numb)
            print(intnumb**2)
            break
        except ValueError:
            print("you should type integer")

# task12()

#Task 13
def create_file():
    with open("hello.txt", "w") as file:
        file.write("Hello, World!")
# create_file()
print("File created successfully!")

# task 14
def read_file():
    try:
        with open("hello.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        return "File not found."
#read_file()

# task 15
def create_file_with_numbers():
    numbers = [1,2,3,4,5,6,7,8,9]
    with open("numbers.txt", "w") as file:
        for n in numbers:
            file.write(str(n) + "\n")

#create_file_with_numbers()

def sum_numbs_file():
    sum = 0
    with open("numbers.txt", "r") as file:
        lines = file.readlines()  # list of all lines
        for i, line in enumerate(lines):
            line = line.strip()  # remove \n
            sum += int(line)
        print(sum)

sum_numbs_file()

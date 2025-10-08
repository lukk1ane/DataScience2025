#Task1
age =  25
name = "Mariam"
print("Task 1")
print("Name: ", name)
print("Age: ", age)
print()

#Task2
length = 10.5
int_length = int(length)
print("Task 2")
print("Type of length: ",type(length))
print("Type og int_length: ", type(int_length))
print()

#Task3
x = 5
y = 10.5
z = "Hello"
print("Task 3")
print(f"x: {x}, y: {y}, z: {z}")
print()



#Task4
def greet(name):
    greeting = "Hello"
    return f"{greeting}, {name}!"

result = greet("Mariam")
print("Task 4")
print(result)
print()


#Task5
def is_even(num):
    return num % 2 == 0
print("Task 5")
print("Is 4 even? " , (is_even(4)))
print("Is 7 even? ", (is_even(7)))
print()


#Task6
print("Task 6")
fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple" : "red", "banana" : "yellow" , "orange" : "orange"}

for fruit in  fruits:
    color = fruit_colors[fruit]
    print(f"{fruit} is {color},", end=" ")

#Task7
print()
print()
squares = [i**2 for i in range (1, 11)]
print("Task 7")
print("Squares from 1 to 10: ", squares)
print()


#Task8
print("Task 8")
print("Numbers between 1 and 20 divisible by 3: ")
for i in range(1, 21):
    if i % 3 == 0:
        print ( i, end = " " )


#Task9
print()
print()
print("Task 9")
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(20)

#Task10
print()
print("Task 10")
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: cannot divide by zero! "
print("divide 10 by 2 :", divide(10, 2))
print("divide 10 by 0 :", divide(10, 0))
print()

#Task11
print("Task 11")

def get_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: Index out of range! "
my_list = [10, 20, 30, 40, 50]
print("Element at index 2: ", get_list_element(my_list, 2))
print("Element at index 10: ", get_list_element(my_list,10))

#Task12
print()
def get_square_from_user():
    while True:
        try:
            user_input = input("Enter an integer: ")
            num = int(user_input)
            square = num ** 2
            print("The square of ", num, " is ", square)
            break
        except ValueError:
          print("Invalid input! Please enter an integer. ")
get_square_from_user()


#Task13
print()
print("Task 13")
try:
    with open('hello.txt', 'w') as file:
        file.write("Hello, World!")
    print("Succesfully wrote to 'hello.txt'")
except Exception as e:
    print()


#Task14
print("Task 14")
try:
    with open('hello.txt', 'r') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: 'hello.txt' does not exist!")

#Task15
print()
print("Task 15")
try:
    with open("numbers.txt", "r") as file:
        lines = file.readlines()
        numbers = [float(line.strip()) for line in lines]
        total = sum(numbers)
        avg = total / len(numbers)
        print("Sum of numbers:", total)
        print("Average of numbers:", avg)
except FileNotFoundError:
    print("Error: 'numbers.txt' not found.")
except ValueError:
    print("Error: File contains non-numeric data.")
except Exception as e:
    print("Unexpected error:", e)











































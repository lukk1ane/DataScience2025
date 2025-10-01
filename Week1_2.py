#Task 1
age=25
name="Barbare"
print(age)
print(name)

#Task2
length=10.5
int_length=int(length)
print(type(length))
print(type(int_length))

#Task3
x=5
y=10.5
z="Hello"
print(f"x:{x},y:{y},z:{z}")

#Task4
def greet(name):
    return f"Hello, {name}!"
print(greet("Barbare"))

#Task5
def is_even(num):
    return num % 2 == 0
print(is_even(4))
print(is_even(7))

#Task6
fruits = ["apple", "banana", "orange"]
fruit_colors ={"apple":"red", "banana":"yellow", "orange":"orange"}
for fruit in fruits:
    print (f"{fruit}: {fruit_colors.get(fruit)}")

#Task7
squares = [val**2 for val in range(1,11)]
print(squares)

#Task8
for i in range(1,21):
    if i%3==0:
        print (i)

#Task9
def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
           print("FizzBuzz")
        elif i%5==0:
           print("Buzz")
        elif i%3==0:
           print("Fizz")
        else:
           print(i)
fizzbuzz(20)

#Task10
def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return  "Error: Division by zero not possible"
print(division(2,2))
print(division(3,4))
print(division(5,0))

#Task11
def list_index_value(l, i):
    try:
        return l[i]
    except IndexError:
        return "Index out of bound"
li=[1,2,3,4,5]
print(list_index_value(li,2))
print(list_index_value(li,20))

#Task12
# while True:
#     try:
#         num = int(input("Enter an integer: "))
#         print("Square:", num ** 2)
#         break
#     except ValueError:
#         print("Invalid input")

#Task13
with open("hello.txt", "w") as file:
    file.write("Hello, World!")
print("Successfully wrote to hello.txt")


#Task14
try:
    with open("hello.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

#Task15
numbers_to_write = [10, 20, 30, 40, 50]  # example numbers
with open("numbers.txt", "w") as file:
    for num in numbers_to_write:
        file.write(f"{num}\n")
print("'numbers.txt' created with sample numbers.")


try:
    with open("numbers.txt", "r") as file:
        lines = file.readlines()
    numbers = [float(line.strip()) for line in lines]

    total = sum(numbers)
    average = total / len(numbers) if numbers else 0

    print("Sum:", total)
    print("Average:", average)

except FileNotFoundError:
    print("Error: 'numbers.txt' does not exist.")
except ValueError:
    print("Error: File contains non-numeric data.")

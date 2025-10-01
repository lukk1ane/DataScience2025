#task1
print("task1")

age = 25
name = "valo"
print(f"{name} is {age} years old")

#task2
print("task2")


length = 10.5
int_lenght = int(length)

print(f"{type(length)}    {type(int_lenght)}")

#task3
print("task3")


x = 5
y = 10.5
z = "hello"

print(f"x:{x} y:{y} z:{z}")

#task4
print("task4")


def greet(name):
    print(f"my name is {name}")

greet("valo")


#task5
print("task5")


def is_even(num):
    if num % 2 == 0 :
        return "true"
    else:
        return "false"

print(is_even(4))
print(is_even(7))

#task6
print("task6")


fruits = ["apple","banana","orange"]
fruit_colors = {"apple":"red","banana":"yellow","orange":"orange"}

for fruit in fruits:
    print(f"{fruit} is {fruit_colors.get(fruit)}")


#task7
print("task7")


squares = []
for i in range(11):
    squares.append(i * i)
print(squares)

#task8
print("task8")


for i in range(20):
    if i % 3 == 0:
        print(i)

#task9
print("task9")


print("task9")
def fizz_buzz(n):
    for i in range(1,n + 1):
        if i % 3 == 0 and i % 5 == 0 :
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizz_buzz(20)


#task10
print("task10")


def division(x,y):
    try:
        print(x / y)
    except:
        print("division by 0")

division(20,0)
division(20,5)

#task11
print("task11")

def list_index(lst,i):
    try:
        print(lst[i])
    except:
        print("index out of range")

l = [1,2,3,4]

list_index(l,1)
list_index(l,10)

#task12
print("task12")

try:
    num = int(input("Enter a number: "))
    square = num ** 2
    print(f"The square of {num} is  {square}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")


#task13
print("task13")

try:
    with open("hello.txt", "w") as file:
        file.write("Hello, World!")

    print("File written successfully!")
except Exception as e:
    print("An error occurred:", e)

#task14
print("task14")

try:
    with open("hello.txt", "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: 'hello.txt' does not exist.")
except Exception as e:
    print("An unexpected error occurred:", e)


#task15
print("task15")


try:
    with open("numbers.txt", "w") as file:
        file.write("10\n20\n30\n40\n50\n")
    print("'numbers.txt' created successfully!")
except Exception as e:
    print("Error creating file:", e)


try:
    with open("numbers.txt", "r") as file:
        numbers = []
        for line in file:
            line = line.strip()
            if line:
                try:
                    num = float(line)
                    numbers.append(num)
                except ValueError:
                    print(f"Warning: '{line}' is not a number and will be skipped.")

    if numbers:
        total = sum(numbers)
        average = total / len(numbers)
        print(f"Sum of numbers: {total}")
        print(f"Average of numbers: {average}")
    else:
        print("No valid numbers found in the file.")

except FileNotFoundError:
    print("Error: 'numbers.txt' does not exist.")
except Exception as e:
    print("An unexpected error occurred:", e)


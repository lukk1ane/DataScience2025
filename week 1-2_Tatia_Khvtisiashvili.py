# TASK 1
age = 25
name = "tatia"
print(name)
print(age)

# TASK 2
length = 10.5
int_length = int(length)
print(type(length))
print(type(int_length))

# TASK 3
x, y, z = 5, 10.5, "Hello"
print(f"x: {x}, y: {y}, z: {z}")


# TASK 4
def greet(name):
    print(f"Hello {name}! :)")


greet(name)


# TASK 5
def is_even(num):
    print(num % 2 == 0)


is_even(4)
is_even(7)

# TASK 6
fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}

for fruit in fruits:
    print(f"{fruit} is {fruit_colors[fruit]}")

# TASK 7
list = [n ** 2 for n in range(1, 11)]
print(list)

# TASK 8
for n in range(1, 21):
    if n % 3 == 0:
        print(n)


# TASK 9
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


# TASK 10
def division(n, m):
    try:
        return int(n / m)
    except ZeroDivisionError:
        return "ups, you tried division by 0"


print(division(6, 0))
print(division(9, 3))


# TASK 11
def find(TheList, index):
    try:
        return TheList[index]
    except IndexError:
        return "this index is out of range."


numbers = [1, 2, 3]
print(find(numbers, 1))
print(find(numbers, 5))


# TASK 12
def square():
    while True:
        try:
            num = int(input("Enter an integer: "))
            print(f"The square of your input: {num ** 2}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


square()


# TASK 13
def write_file():
    with open("hello.txt", "w") as file:
        file.write("Hello, World!")
    print("Successfully wrote to hello.txt")


write_file()


# TASK 14
def read_file():
    try:
        with open("hello.txt", "r") as file:
            content = file.read()
            print("This is what's inside the file: ", content)
    except FileNotFoundError:
        print("File not found.")


read_file()


# TASK 15
def process():
    try:
        with open("numbers.txt", "r") as file:
            numbers = []
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")

            if numbers:
                total = sum(numbers)
                avg = total / len(numbers)
                print("Sum:", total)
                print("Average:", avg)
            else:
                print("No valid numbers found.")
    except FileNotFoundError:
        print("Error: numbers.txt file not found.")


with open("numbers.txt", "w") as file:
    file.write("10\n20\n30\n40\n")

process()

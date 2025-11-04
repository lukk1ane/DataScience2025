# Task 1
age = 25
name = 'Eka'
print(age, name)

# Task 2
length = 10.5
int_length = int(length)
print(length, int_length)

# Task 3
x = 5
y = 10.5
z = 'Hello'
print(("x: {}, y: {}, z: {}".format(x, y, z)))


# Task 4
def greet(name):
    print(name)


greet(name)


# Task 5
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(4), is_even(7))

# Task 6
fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}
for fruit in fruits:
    print(f"{fruit} is {fruit_colors[fruit]}")

# Task 7
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

# Task 8
for nums in range(1, 20):
    if nums % 3 == 0:
        print(nums)


# Task 9
def fizz_buzz(n):
    for nums in range(1, n):
        if nums % 15 == 0:
            print('fizzbuzz')
        elif nums % 3 == 0:
            print('fizz')
        elif nums % 5 == 0:
            print('buzz')
        else:
            print(nums)


fizz_buzz(20)


# task 10
def division(a, b):
    try:
        print(int(a / b))
    except ZeroDivisionError:
        print("divisor cannot be zero")


division(10, 3)
division(10, 0)

# task 11
list = [1, 2, 3, 4, 5, 6]


def list_index(x):
    try:
        print(list[x])
    except IndexError:
        print("Out of list's range")


list_index(2)


# Task 12
def inp():
    while True:
        try:
            i = int(input("write a number: "))
            print(f"square is: {i ** 2}")
        except ValueError:
            print("the input is not an integer")


# inp()

# Task 13
def write_file():
    with open("hello.txt","w") as file:
        file.write("Hello, world!")
    print("successfully wrote to the hello.txt file")


write_file()

# Task 14
def read_file():
    try:
        with open("hello.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("file does not exist")

read_file()

# Task 15
def read_numbers():
    sum_txt = 0
    number_of_int_lines = 0
    try:
        with open("numbers.txt", "r") as file:
            for line in file:
                try:
                    number = float(line.strip())
                    sum_txt += number
                except ValueError:
                    print(f"skipping line: '{line.strip()}'")
    except FileNotFoundError:
        print("file does not exist")
    with open("numbers.txt", "r") as file:
        for line in file:
            integer_lines = line.strip()
            if integer_lines.isdigit():
                number_of_int_lines += 1
            average = sum_txt / number_of_int_lines
    print(average)
    print(sum_txt)

read_numbers()
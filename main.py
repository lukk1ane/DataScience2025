# 1

age = 25
name = "luka"

print(name)
print(name)

# 2

length = 10.5
int_length = int(length)

print(length)
print(int_length)

# 3

x = 5
y = 10.5
z = "hello"

print(f'x: {x}, y: {y}, z: {z}')


# 4

def greet(name):
    return f'hello {name}'


print(greet('luka'))

# 5


def is_even(num):

    if num % 2 == 0:
        return True

    return False

print(is_even(4))
print(is_even(7))

# 6

fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}


for fruit in fruits:
    print(fruit_colors[fruit])

# 7

l_squared = [i * i for i in range(1, 10 + 1)]

print(l_squared)

# 8

l_3div = [i for i in range(1, 20 + 1) if i % 3 == 0]

print(l_3div)

# 9


def fizz_buzz(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i}: fizzbuzz")
        elif i % 3 == 0:
            print(f"{i}: fizz")
        elif i % 5 == 0:
            print(f"{i}: buzz")

fizz_buzz(20)

#10


def div(n1, n2):
    try:
        return n1 / n2
    except ArithmeticError as e:
        print(e)
        return None


div(1, 0)
div(15, 5)

# 11


def get_val(lst, idx):
    try:
        return lst[idx]
    except Exception as e:
        print("list index out of bound")
        return None

# 12


num = None


def input_int():

    num = input("input an integer: ")

    if "." in num:
        raise TypeError("Not an integer")

    try:
        num = int(num)
    except Exception as e:
        raise TypeError("Not an integer")

    return num


while num is None:

    try:
        num = input_int()
    except TypeError as e:
        print("incorrect type, try again")

print(num * num)

# 13

f = open("hello.txt", "w")
f.write("hello world")
f.close()

# 14

try:
    f = open("hello.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("file does not exist")


# 15

f = open("numbers.txt", "r")

sum = 0
l = 0

for line in f.readlines():
    sum += float(line)
    l += 1.0

print(div(sum, l))


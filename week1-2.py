# task 1
age = 25
name: str = "Tatia"
print(age)
print(name)

# task 2
length = 10.5
int_length = int(length)
print(type(length))
print(type(int_length))

# task 3
x, y, z = 5, 10.5, 'Hello'
print(f'x: {x}, y: {y}, z: {z}')

#task 4
def greet(name):
    print(f'Hello, {name}')

greet("Tatia")

#task 5
def is_even(num):
    if num%2==0:
        return True
    return False

print(is_even(4))
print(is_even(7))

# task 6
fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}

for i in fruits:
    print(f'the color of {i} is {fruit_colors[i]}')

#task 7
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers_squared = [i**2 for i in numbers]
print(numbers_squared)

#task 8
for i in range(1, 21):
    if i%3==0:
        print(i)

# task 9
def fizz_buzz(n):
    for i in range(1, n+1):
        if i%15==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(20)

# task 10
def div(n, m):
    try:
        print(n/m)
        return n/m
    except ZeroDivisionError:
        print("Can't divide by 0")

div(10,5)
div(13,3)
div(7,0)

# task 11
def list_index(lst, i):
    try:
        print(lst[i])
        return lst[i]
    except IndexError:
        print("Index out of range")

list_index([1,4,7,8], 2)
list_index([2,3,5], 5)

# task 12
b = "a"
while b=="a":
    a = input()
    try:
        b = int(a)
    except ValueError:
        print("Please type in a number")
print(b**2)

# task 13
with open('hello.txt', 'w') as f:
    f.write("Hello, World!")

print("Success!")

# task 14
try:
    f = open('hello.txt')
    print(f.read())
except FileNotFoundError:
    print("The file doesn't exist")

# task 15
with open('numbers.txt', 'w') as f:
    for i in range(1, 21):
        f.write(f'{i}\n')

try:
    nums = []
    with open("numbers.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    nums.append(float(line))
                except ValueError:
                    continue
    summ = sum(nums)
    average = summ / len(nums)
    print(f'sum is {summ}')
    print(f'average is {average}')

except FileNotFoundError:
    print("The file doesn't exist")

# Task 1

age = 25
name = "name"
print(age)
print(name)

# Task 2

length = 10.5
int_length = int(length)
print(type(length))
print(type(int_length))

# Task 3

x = 5
y = 10.5
z = "Hello"
print(f"x:{x} y:{y} z:{z}")

# Task 4
def greet(name):
    return "Greeting"
print(greet("Ioane"))

# Task 5
def is_even(num):
    if (num % 2 == 0 ) : return True
    else : return False
print(is_even(4))
print(is_even(7))

# Task 6
fruits = ["apple" , "banana" , "orange"]
fruit_colors = {"apple" : "red" , "banana":"yellow" , "orange" : "orange"}

for x in fruits:
    print(x,fruit_colors.get(x))

# Task 7

nums = [1,2,3,4,5,6,7,8,9,10]
sqrs = [x ** 2 for x in nums]
print(sqrs)

# Task 8
for x in range(21):
    if(x % 3 == 0 and x != 0) : print(x)

# Task 9

def fizz_buzz(n):
    for x in range(n+1):
        if x == 0 : print("```")
        elif (x % 3 == 0 and x % 5 == 0) : print("FizzBuzz")
        elif (x % 3 == 0) : print("Fizz")
        elif (x % 5 == 0) : print("Buzz")
        else : print(x)

fizz_buzz(20)

# Task 10
def div(x,y):
    try: res = x / y
    except ZeroDivisionError : print("Divided by Zero!")
    else : print(res)

div(3,3)
div(3, 0)

# Task 11
l = [4,5,6]
def search(list, i):
    try:
        print(list[i])
    except IndexError : print("Index out of bounds")


search(l,2)
search(l,5)

# Task 12
while True :
    raw = input("Enter your number :")
    try:
        input = int(raw)
        square = input ** 2
        print(square)
        break
    except ValueError :
        print("Not an Integer . Please enter valid integer")

# Task 13
    """
 with open('hello.txt', 'w') as file:
     file.write("Hello,World!")
     print("Successfully written")
     """

# Task 14
with open ('hello.txt' , 'r') as file:
    content = file.read()
    print(content)

# Task 15
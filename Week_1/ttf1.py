name = "andria "
age = 25

print(f"{name} is {age} years old.")

length = 10.5 
int_length = int(length)
print(f"length in float: {length}, length in int: {int_length}")

x, y, z = 5, 10.5, 'hello'

print(f"x: {x}, y: {y}, z: {z}")

def greeting(name):
    return f"Hello, {name}!"


greeting("Andria")

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
is_even(4)
is_even(5)  

fruits = ['apple', 'banana', 'orange']

fruit_colors = {
    'apple': 'red',
    'banana': 'yellow',
    'orange': 'orange'
}

for i in fruit_colors:
    print(f"{i} is {fruit_colors[i]}")
    
squares = [x**2 for x in range(1, 11)]

print(squares)


for i  in  range(1, 21):
    if i % 3== 0:
        print(i)
        
def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)    

fizz_buzz(30)
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(divide(10, 2))
print(divide(10, 0))
    
def list_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: Index out of range."
    

        
while True:
    user_input = input("Enter a number : ")
    try:
        number = int(user_input)
        print(f"You entered: {number**2}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
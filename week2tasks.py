#task1

a = 25
name = "erekle"

print(f"My name is {name} and I am {25} years old")

#task2

length = 10.5
int_length = int(length)

print(f"{length}  {int_length}")

#task3

x = 5
y = 10.5
z = 'Hello'

print(f"x: {x}, y: {y}, z: {z}")


#task4

def greetings(name):
    return "Greetings " + name

name = "erekle"
print(greetings(name))


#task5

def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))


#task6

fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}

for i in fruits:
    print(fruit_colors[i])


#task7

for i in range(1, 11):
    print(i**2)


#task8

for i in range(20):
    if i % 3 == 0:
        print(i)


#task9

def fizz_buzz(n):
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 ==0:
            if i % 3 == 0 and i % 5 ==0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            else:
                print("Buzz")
        else:
            print(i)
fizz_buzz(20)


#task10

def divisioncheck(a, b):
    try:
        return (a / b)
    except:
        return("Division by zero exception")

print(divisioncheck(1,0))
print(divisioncheck(1,1))


#task11

def indexcheck(lst, i):
    try:
        return lst[i]
    except:
        return ("Index out of bound exception")
    
lst = [1,2,3,4,5]
print(indexcheck(lst, 2))
print(indexcheck(lst, 10))



#task12


while True:
    user_input = input("Enter your number: ")
    try:
        number = int(user_input)   
        print(number ** 2)         
        break                      
    except ValueError:             
        print("Invalid input, please enter a number.")



#task13


with open("hello.txt", "a") as f:
    f.write("Hello World!")
    print("Success")


#task14

try:
    with open("hello.txt", "r") as f:
        a = f.read()
        print(a)
except FileNotFoundError:
    print("File was not found")



#task15

with open("numbers.txt", "a") as f:
    for i in range(101):
        if i == 100:
            f.write(f"{i}")
        else:
            f.write(f"{i}\n")

sum = 0
with open("numbers.txt", "r") as f:
    for i in f:
        sum += int(i.strip())

print(sum)















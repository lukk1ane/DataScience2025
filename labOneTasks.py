from pandas import RangeIndex

# task1
age=25
name="Mariam"

print(age,name)

# task2
length=10.5
int_length=int(length)

print(type(length),type(int_length))

# task3

x,y,z=5, 10.5, "hello"
print(f'x : {x} , y : {y}, z : {z}')

# task4

def greet(name):
    print(f'Hello {name}')

greet("Mariam")

# task5

def is_even(num):
    return num%2==0

print(is_even(4),is_even(7))


# task6

fruits=["apple","banana","orange"]
fruit_colors={"apple":"red", "banana":"yellow","orange":"orange"}

for fruit in fruits:
    print(f'Color of the {fruit} is {fruit_colors[fruit]}')

# task7

squares=[x**2 for x in range(1,11)]

print(squares)

# task8

for x in range(1,21):
    if x%3==0:
        print(x, end=" ")

# task9

def fizz_buzz(n):
    for x in range(1,n+1):
        if x%3==0 and x%5==0:
            print("FizzBuzz")
        elif x%3==0:
            print("Fizz")
        elif x%5==0:
            print("Buzz")
        else:
            print(x)

fizz_buzz(20)

# task10

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Nope"

print(division(1,2),division(1,0))

# task11

def value_at_index(list,index):
    try:
        return list[index]
    except IndexError:
        return "Nope"

print(value_at_index([1,2,3],1),value_at_index([1,2,3],5))

# task12

while True:
        print("Enter a number: ")
        input1 = input()
        try:
            number1=int(input1)
            print(number1**2)
            break
        except ValueError:
            print("Not Valid, Try again")

# task13

with open("hello.txt", "w") as file:
    file.write("Hello, World!")

print("File created")

# task14

try:
    with open("hello.txt","r") as file:
        read=file.read()
        print(read)
except FileNotFoundError:
    print("File doesnt exist")

# task15

numbers=[1,2,3,4,5,6,7,8,9,10]

with open("numbers.txt","w") as file:
    for n in numbers:
        file.write(str(n) + "\n")

try:
    with open("numbers.txt", "r") as file:
        total=0
        count=0
        for line in file:
            try:
                total+=int(line.strip())
                count+=1
            except ValueError:
                print("Not integer")
        print(total)
        print(total/count)

except FileNotFoundError:
    print("File doesnt exist")
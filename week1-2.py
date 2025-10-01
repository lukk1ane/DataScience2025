#task 1
age = 25
name ="teona"
print(f"{age},{name}")

#task2
length=10.5
in_length=int(length)
print(f"{length},{in_length}")

# #task3
x,y,z=[5, 10.5 , "Hello"]
print(f"x:{x}, y:{y} , z:{z}")

# #task4
def greet(name):
    return f"Hello {name}"
    
print(greet("Teona"))

# #task5
def is_even(num):
    if num%2==0:
        return True
    else:
        False
print(is_even(4))

# #task6
fruits=["apple","banana","orange"]
fruit_colors={"apple":"red" , "banana":"yellow", "orange":"orange"}

for fruit in fruits:
   print(fruit , "is" , fruit_colors[fruit]) 


# #task7
squares = [x**2 for x in range(1, 11)]
print(squares)



# #task8
for num in range(1,22):
    if num%3==0:
        print(num) 


# #task9
def fizz_buzz(n):
    for num in range(1,n+1):
     if num%3==0 and num%5==0:
        print ("FizzBuzz")
     elif num%3==0:
        print("Fizz")
     elif num%5==0:
        print("Buzz")

print(fizz_buzz(20))

 #task10
def divisible(a,b):
   try:
      return a/b
   except ZeroDivisionError:
        return "Error: Division by zero is not allowed"

print(divisible(4,2))
print(divisible(3,0))

# #task11
def list_index(list,index):
   try:
        return list[index]
   except IndexError:
        return "Error: Index out of range"


numbers = [3, 6 ,9]

print(list_index(numbers, 1))  
print(list_index(numbers, 5))  


#task12
while True:
  user_input=input("Enter number: ")
  try:
    make_int= int(user_input)
    print(make_int**2)
    break
  except ValueError:
    print("invalid input")

#task13
with open("hello.txt", "w") as file:
    file.write("Hello, World!")

print("file 'hello.txt' written successfully")

#task14
try:
    with open("hello.txt", "r") as file:
        content = file.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    print("Error: 'hello.txt' does not exist!")

#task15
try:
    with open("numbers.txt", "r") as file:
        numbers = []
        for line in file:
            line = line.strip()  
            if line:  # skip empty lines
                numbers.append(float(line))  # convert to float

    total = sum(numbers)
    average = total / len(numbers)
    print("Sum:", total)
    print("Average:", average)

except FileNotFoundError:
    print(" 'numbers.txt' doesnot exist")
except ValueError:
    print("File contains non-numeric data")

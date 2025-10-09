#task1
age = 25
name = "Liza"
print(age)
print(name)

#task2
length = 10.5
int_length = int(length)
print(type(length))
print(type(int_length))

#task3
x, y, z = 5, 10.5, 'Hello'
print(f"x:{x}, y:{y}, z:{z}")

#task4
def greet(name):
    print(f'Hello {name}')
greet('liza')

#task5
def isEvenNum(num):
    if num % 2 == 0:
        return True
    return False
print(isEvenNum(2))

#task6
fruits = ['apple','banana','orange']
fruit_colors = {'apple':'red', 'banana':'yellow', 'orange':'orange'}
for i in fruits:
    color = fruit_colors.get(i)
    print(f"{i} : {color}")

#task7
i = 1
myarr = []
while i <= 10:
    myarr.append(i)
    i += 1

my_list = [mynum**2 for mynum in myarr]
print(my_list)

#task8
for i in range(1,20):
    if i % 3 == 0:
        print(i)

#task9
def fizz_buzz(n):
    for i in range(1,n):
        if i %3 == 0 and i% 5 == 0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizz_buzz(10)

#task10
def mydiv(num1, num2):
    try:
        result = num1/num2
        return result
    except ZeroDivisionError:
        print('Cannot divide by zero.')
        return None


print(mydiv(6,2))
#print(mydiv(6,0))

#task11
def returnIndex(mylist, index):
    try:
        for i in range(len(mylist)):
            if i == index:
                return mylist[i]
    except IndexError:
        print('Index out of bounds.')
        return None


mylist = ['1', '2', '3', '4']
index = 6
#print(returnIndex(mylist, index))

#task12
def mysquare():
   num = input("input a number: ")
   try:
       num = int(num)
       return num**2
   except ValueError:
       print('Not an integer.')

print(mysquare())

#task13
with open('hello.txt', 'w') as file:
    file.write("Hello, World!")
    print("Text successfully written into the file")
#task14
try:
    with open('hello.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('file not found.')

#task16
mynums = ['1','2','3','4','5','6','7','8','9','10']
with open('numbers.txt', 'w') as file:
    for i in range(len(mynums)):
        file.write(mynums[i] + '\n')

total = 0
valid_line_count = 0
try:
    with open('numbers.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    number = int(line)
                    total += number
                    valid_line_count += 1
                except ValueError:
                    print(f"Warning: Skipping non-numeric value '{line}'")

    if valid_line_count > 0:
        avg = total / valid_line_count
        print(f"Sum: {total}, Average: {avg}")
    else:
        print("No valid numeric data found to calculate sum and average.")
except FileNotFoundError:
    print("Error: 'numbers.txt' file not found.")


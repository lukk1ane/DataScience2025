# task 1
age = 25
name = "dato"
print(f"{age},{name}")

# task 2
length = 10.5
int_len = int(length)
print(f"{type(length)},{type(int_len)}")

# task 3
x = 5
y = 10.5
z = 'Hello'
print(f"x : {x} y : {y}  z : {z}")


# task 4
def greet(name):
    return f"yo, {name}"


# task 5
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(4))
print(is_even(7))

# task 6
fruits = ["apple", "banana", "orange"]
fruit_colors = {"apple": "red",
                "banana": "yellow",
                "orange": "orange"}

for fruit in fruits:
    print(fruit + " " + fruit_colors[fruit])

# task 7
res = [x ** 2 for x in range(1, 11)]
print(res)


# task 8
def task_8():
    for i in range(1, 20):
        if i % 3 == 0:
            print(i)


task_8()


# task 9

def fizz_buzz(n):
    for num in range(1, n):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)


# task 10

def errorHandler(num1, num2):
    res = 0
    try:
        res = num1 / num2
    except ZeroDivisionError:
        print("cant divide by 0")
        return None
    return res


print(errorHandler(2, 0))


# task 11

def list_index(lst, ind):
    try:
        res = lst[ind]
    except IndexError:
        print("Invalid index")
        return None
    return res


list = [1, 2, 3, 4, 5]
print(list_index(list, 2))
print(list_index(list, 24))
print(list_index(list, -12))


# task 12

def task_12():
    num = input("Write a number: ")

    try:
        res = int(num)
    except:
        print("invalid input")
        return None
    res **= 2
    print(res)
    return res


task_12()


# task 13

def file_writing():
    with open("hello.txt", 'w') as file:
        file.write("Hello, World!")
        print("File writing was Succesfull.")
        file.close()


file_writing()


# task 14

def file_reading():
    with open("hello.txt", 'r') as file:
        content = file.read()
    print(content)


file_reading()


# task 15

def processing_file():
    result = 0
    with open("numbers.txt", 'r') as file:
        for line in file:
            try:
                line = int(line)
                result += line
            except:
                print("Invalid input")
                return None
    return result


print(processing_file())

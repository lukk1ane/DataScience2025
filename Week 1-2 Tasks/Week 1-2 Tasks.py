#1
age = 25;
name = "Luka";
print(age, name);

#2
length = 10.5;
int_length = int(length);
print(type(length), type(int_length));

#3
x = 5;
y = 10.5;
z = "Hello";
print(f"x = {x}, y = {y}, z = {z}");

#4
def greet(name):
    print(f"Hello, {name}!");
print(greet("Luka"));

#5
def is_even(num):
    return num % 2 == 0;
print(is_even(4));
print(is_even(7));

#6
fruits = ["apple", "banana", "orange"];
fruit_colors = {"apple": "red", "banana": "yellow", "orange": "orange"}
for fruit in fruits:
    print(fruit + " -> " + fruit_colors[fruit]);

#7
squares = [i**2 for i in range(1,11)];
print(squares);

#8
for x in range(1,21):
    if(x % 3 == 0):
        print(x);

#9
def fizz_buzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i);
fizz_buzz(20);

#10
def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("arsheidzleba");
div(1, 2);
div(1, 0);

#11
def val(list, index):
    try:
        return list[index];
    except IndexError:
        print("gacda sazgvrebs dzmao");
val([1,2,3,4,5], 2);

#12
try:
    user_input = int(input("Enter an integer: "))
    print(user_input ** 2)
except ValueError:
    print("integeri sheiyvane bijo");

#13
with open("hello.txt", "w") as f:
    f.write("zd all");
    print("daiprinta");

#14
try:
    with open("hello.txt", "r") as f:
        out = f.read()
        print(out);
except FileNotFoundError:
    print("file not found");

#15
try:
    with open("numbers.txt", "r") as f:
        nums = f.readlines();
        nums = [float(n.strip()) for n in nums];
        total = sum(nums);
        avg = total / len(nums);
        print(total);
        print(avg);
except FileNotFoundError:
    print("file not found");
except ValueError:
    print("integeri sheiyvane bijo");




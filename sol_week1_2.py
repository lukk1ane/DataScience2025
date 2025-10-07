#task 1
age = 19
name = "Annie"
print(f"age = {age}, name = {name}")

#task 2
length = 10.5
int_length = int(length)
print(f"length: {type(length)}, int_length: {type(int_length)}")

#task 3
x=5
y=10.5
z="Hello"
print(f"x: {x}, y: {y}, z: {z}")

#task 4
def greet(name):
    return f"Hello, {name}!"
print(greet("Hikaru"))

#task 5
def is_even(num):
    if num%2==0: 
        return True
    else: 
        return False
print(is_even(4), is_even(7))

#task 6
fruits=["apple","banana","cherry"]
fruit_colors={"apple":"red","banana":"yellow","cherry":"red"}
for fruit in fruits:
    print(f"{fruit } is {fruit_colors[fruit]}")

#task 7
list = [i**2 for i in range(1,11)]
print(list)

#task 8
for i in range (1,21):
    if i%3==0:
        print(i)

#task 9
def fizz_buzz(n):
    for i in range( 1,n+1):
        if i%3==0 and i%5==0:
            print("FIzzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else: 
            print(i)

fizz_buzz(20)

#task 10
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    
print(div(5,3))
print(div(450,45))
print(div(5,0))

#def task 11
def get_element(lst, i):
    try:
        return lst[i]
    except IndexError:
        return "Error: Index out of range"
    
lst = [1,2,3,4,5,6,7]        
print(get_element(lst,3))
print(get_element(lst,0))
print(get_element(lst,7))   


#task 12
while True:
 try:
    inp = int(input("enter a number: "))
    print(inp**2)
    break
 except ValueError:
    print("Error: invalid input. Please enter a valid integer") 
       
#task 13
with open('output.txt','w') as file:
    file.write("Hello,World!")

print("File written successfully")   


#task 14
try: 
   with open('output.txt','r') as file: 
     content= file.read()
     print(content)
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("read from file created in task13, HELLOOO WORLldDDD")



#task 15
try:
  def write(n):
    with open('number.txt','w') as file:
        for i in range(1,n+1):
           file.write(f"{i}\n")

  write(10)

  with open('number.txt','r') as file:
   content = [int(line.strip()) for line in file]
    
        
  total =sum(content)
  avg= total/len(content)
  print(f"sum: {total}, average: {avg}")

except FileNotFoundError:
    print("Error: File not found")
except ValueError:
    print("Error: File contains non-numeric data")
finally:
    print("DONE ehhehe")


#Task 1
age=19
name="Gvantsa"  
print(f"My name is {name} and I am {age} years old.")

#Task 2
length=10.5
int_length=int(length)
print(type(int_length))
print(type(length))

#Task 3
[a,b,c]=[5,10.5,"Hello"]
print("a:",a, ", b:",b, ", c:",c)

#Task 4
input = input("Enter your name: ")

def greet(name):
    print("Hello, " + name )
greet(input)

#Task 5
def is_even(numb):
    if numb%2==0: return True
    else: return False

print(is_even(4))
print(is_even(7))

#Task 6
fruits =["apple", "banana", "orange"]
fruit_colors ={"apple":"red", "banana":"yellow", "orange":"orange"}
for i in fruits:
    print(f"{i} is {fruit_colors[i]}")

#Task 7
res = [ i**2 for i in range(1,11)]
print(res)

# #Task 8
for i in range (1, 21):
  if i%3==0: print(i)

#Task 9
a=1
while a<=100 : # Loop from 1 to 100
    if a%3==0 and a%5==0 : print("FizzBuzz") # Check divisibility by both 3 and 5 first
    elif a%3==0 : print("Fizz") # Check divisibility by 3
    elif a%5==0 : print("Buzz") # Check divisibility by 5
    else : print(a) # Print the number if not divisible by 3 or 5
    a+=1 # Increment the counter

#Task 11
try: 
    def list_index(lst, ind):
        for i in range (len(lst)):
            if i==ind: return lst[i]
except IndexError: print("Error: Index out of bounds")        
finally: print("Execution completed.")

print(list_index([1,2,3,4,5], 2))


#Task 12
try:
    input_num = int(input("Enter a number: "))
    square = input_num ** 2
    print(square)
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
finally:
    print("here comeeess the suunnnn pararaaraammm!!!!!!")

#Task 13
with open("sample.txt", "w") as file:
    file.write("Hello, World!")

print("Wrote successfullyyyy")

#Task 14
try:
    with open("sample.txt", "r") as file:
        content=file.read()
        print(content)
except FileNotFoundError: print("File doen't exist")
finally: print("parararaaaammmm")

#Task 15
try:
    def write_numbers(nums):
        with open("numbers.txt", "w") as file:
            for i in nums:
                file.write(f"{i}\n")

    write_numbers([2,3,4,532,3])
        
    with open("numbers.txt", "r") as file:
        numbers = [float(i.strip()) for i in file] 

        sum=sum(numbers)
        avg=sum/len(numbers)
        print("Sum:", sum)  
        print("Average:", avg)

except FileNotFoundError: print("File doen't exist")
except ValueError: print("Invalid value")
finally: print("parararaaaammmm")
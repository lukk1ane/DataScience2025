class habit_data:
    #Task 1
    age = 25 
    name = "Dachi"
    
    #Task 2
    
    length = 10.5 
    int_length = int(length)
    
    #Task 3
    
    x, y, z = 5 , 10.5, "Hello"
    
    print('x:',x,", y:",y,"z:", z )
    
    #Task 4
    def greet(name):
        return print("Hello", name)
    greet(name) 
    
    #Task 5
    
    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False 
        
    is_even(10)
    
    #Task 6
    
    fruits = ["apple", "banana", "orange"]
    
    fruit_colors = {"apple": "red", "banana" : "yello", "orange" : "orange"}
    
    for key, value in fruit_colors.items():
        print(key, value)
    
    #Task 7
    
    num_lst = [i * i for i in range(1, 11)]
    print(num_lst)
    
    #Task 8
    
    for i in range(1,21):
        if i % 3 == 0:
            print(i)
            
    #Task 9
    
    def fizz_buzz(n):
        for i in range(1, n):
            if i % 3 ==0 and i % 5 == 0:
                print("FizzBuZZ")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else: 
                print(i)
    fizz_buzz(21)

    #Task 10
    def return_div(a,b):
        try:
            return(a / b)
        except ZeroDivisionError:
            return "ZeroDivisionError"
        
    return_div(18, 2)
    
    #Task 11
    
    def return_nth(some_lst, index):
        try:
            return some_lst[index] 
        except IndexError:
                return "Index out of bounds"
        
    #Task 12 
    
    def read_square(): 
        try: 
            user_input = input("Enter an integer")
            int_input = int(user_input)
            
            square = int_input* int_input 
            
            
            print(square)
            
        except ValueError:
            print("invalid input")
            
    
        
            
        
        
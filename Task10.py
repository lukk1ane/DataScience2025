def division(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("Dvision by zero")

print(division(1,0))
print(division(2,1))
print(division(0,1))
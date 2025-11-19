# Task 12
resume = True
while resume:
    try:
        user_input = int(input("Enter a number: "))
        print(f"The square of your number is {user_input**2}")
        resume = False
    except ValueError:
        print("Incorrect type provided")


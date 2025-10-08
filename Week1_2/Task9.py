def fizz_buzz(n):
    for i in range(n):
        if (i + 1)%3==0 and (i + 1)%5==0: print("FizzBuzz")
        else:
            if (i + 1)%3==0: print("Fizz")
            else:
                if (i + 1)%5==0: print("Buzz")
                else: print(i+1)

fizz_buzz(20)
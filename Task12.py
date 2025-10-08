
while(True):
    try:
        val=int ( input("write number: ") )
    except ValueError:
        print("That is not a number")
    else: break
print(val**2)
with open('Hello.txt', 'w') as file:
    file.write("Hello, World!")
    print("success")


try:
    with open('Hello.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
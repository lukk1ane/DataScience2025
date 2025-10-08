try:
    with open("hello.txt", "r") as file:
            content=file.read()
except FileNotFoundError:
    print("File Doesn't exists")
else: print(content)
fruits=["apple" , "banana" , "orange"]
fruit_colors={"apple" : "red" , "banana": "yellow" , "orange":"orange"}
for fruit in fruits:
    print(fruit, fruit_colors.get(fruit))

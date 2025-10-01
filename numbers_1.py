with open('numbers.txt', 'w') as file:
    for i in range(1, 11):
        file.write(f"{i}\n")
    print("Numbers written successfully.")
    
    
def insights_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file.readlines()]
            total = sum(numbers)
            average = total / len(numbers) if numbers else 0
            return f"total: {total}, average: {average}"
                
            
    except FileNotFoundError:
        return "File not found."
    except ValueError:
        return "File contains non numerical values."

print(insights_from_file('numbers.txt'))

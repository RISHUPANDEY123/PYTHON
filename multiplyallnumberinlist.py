numbers = [3,7,2,1,-2]
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply(numbers))
x = int(input("enter the value of x:"))
y = int(input("enter the value of y:"))
def sum(x, y):
    sum = x + y
    if sum in range(10,20):
        return 15
    else:
        return sum
print(sum(x,y))
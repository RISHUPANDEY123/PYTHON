n = int(input("enter a number"))
def squresum_of_number(n):
    sum = 0
    for i in range (1,n+1):
        sum = sum + (i*i)
    return sum
print(squresum_of_number(n))        
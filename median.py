a = float(input("Input a number: "))
b = float(input("Input a number: "))
c = float(input("Input a number: "))
if a > b:
     if a < c:
        median = a
     elif b > c:
        median = b
     else:
        median = c
else:
     if a > c:
        median = a
     elif b < c:
        median = b
     else:
        median = c

print("The median is", median)

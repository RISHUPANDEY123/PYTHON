x = int(input("enter value for x: "))
y = int(input("enter value for y: "))
z = int(input("enter value for z: "))

if x == y == z:
	print("equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")
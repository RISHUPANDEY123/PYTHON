num = int(input("enter a number:"))
result = list(map(lambda x: 2 ** x, range(num)))
for i in range(num):
   print("2 raised to power",i,"is",result[i])
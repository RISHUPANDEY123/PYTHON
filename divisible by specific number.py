list1 = [15,30,35,70,90,135]
result =list(filter(lambda x: (x % 5 == 0),list1))
print("divisible by 5",result)
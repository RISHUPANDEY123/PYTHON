list1 = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: (x % 15 == 0), list1))
print("Numbers divisible by 15 are",result)

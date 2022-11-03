array = [-1, 2, -5, -7, 8, 3,0 ]
result = sorted(array, key = lambda i: 0 if i == 0 else -1 / i)
print("Rearrange positive and negative numbers of given array :")
print(result)

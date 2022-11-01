def in_group_value(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(in_group_value([1, 2, 7, 3], -3))
print(in_group_value([5, 9, 3], 9))
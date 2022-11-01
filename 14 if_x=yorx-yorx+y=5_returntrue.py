def test_number5(x, y):
   if x == y or (x-y) == 5 or (x+y) == 5:
       return True
   else:
       return False
print(test_number5(6,7))
print(test_number5(4,1))

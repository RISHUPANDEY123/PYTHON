def test_different(num):
  if len(num) == len(set(num)):
    return True
  else:
    return False;
print(test_different([1,5,7,9,6,7]))
print(test_different([2,4,5,3,7,9]))

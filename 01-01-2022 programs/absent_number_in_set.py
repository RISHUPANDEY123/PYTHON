def absent_digits_in_set(n):
  all_nums = set([0,1,2,3,4,5,6,7,8,9])
  n = set([int(i) for i in n])
  n = n.symmetric_difference(all_nums)
  n = sorted(n)
  return n
print(absent_digits_in_set([4,5,-3,6,7,2,2,3,6,7]))

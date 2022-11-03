def addition_subtrction(x, y):
    return x + y, x - y
 
nums1 = [7,8,9,0]
nums2 = [0,5,4,3]
print(nums1)
print(nums2)
result = map(addition_subtrction, nums1, nums2)
print(list(result))

def odd_product(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        if product & 1:
          return True
  return False          
nums1 = [2, 4 ,  10]
nums2 = [1, 6, 4, 7, 8]
nums3 = [1, 3, 5, 7, 9]
print(nums1, odd_product(nums1));
print(nums2, odd_product(nums2));
print(nums3, odd_product(nums3));
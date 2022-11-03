def test(nums):
    return nums.count(19) == 2 and nums.count(5) >= 3
nums = [19,15,5,3,5,5,2]
print(nums)
print(" two occurrences of nineteen and at least three occurrences of five in the list:")
print(test(nums))
def sum_of_distinct_pairs(arr):
    result = 0
    i = 0
    while i<len(arr):
        result+=i*arr[i]-(len(arr)-i-1)*arr[i]

        i+=1
    return result
print(sum_of_distinct_pairs([9,4,7]))
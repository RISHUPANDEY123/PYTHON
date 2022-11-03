def list_Of_lists(str):
    result = map(list, str)
    return list(result)

list1 = ["123", "456", "789", "0123"]
print(list1)
print(list_Of_lists(list1))

def concatenate_list_element(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_element([0,1,2,3,4,5]))
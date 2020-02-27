test_list = [1, 4, 5, 5, 5, 9, 1] 
original_set = set() 
result = [] 
for idx, val in enumerate(test_list): 
    if val not in original_set: 
        original_set.add(val)          
    else: 
        result.append(idx)
print("The list of elements is :  " + str(test_list)) 

print("The list of duplicate elements is :  " + str(result)) 

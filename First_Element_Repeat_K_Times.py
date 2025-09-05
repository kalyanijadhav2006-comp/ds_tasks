def first_element_k_times(arr, k):
    
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    
    for num in arr:
        if count[num] == k:
            return num
    
    return -1


arr = [3, 1, 4, 4, 5, 2, 6, 1, 4]
k = 2
print("Input array:", arr)
print("k =", k)
print("Output:", first_element_k_times(arr, k))
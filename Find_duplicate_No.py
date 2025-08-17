def findDuplicate(arr):
    low, high = 1, len(arr) - 1  # numbers are in [1, n]
    
    while low < high:
        mid = (low + high) // 2
        count = sum(num <= mid for num in arr)
        
        if count > mid:
            high = mid  # duplicate is in the left half
        else:
            low = mid + 1  # duplicate is in the right half
    
    return low

# Example
arr = [3, 1, 3, 4, 2]
print("Duplicate number:", findDuplicate(arr))

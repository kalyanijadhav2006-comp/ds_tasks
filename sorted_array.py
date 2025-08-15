def sort(a):
    low = 0
    mid = 0 
    high = len(a) - 1
    
    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            a[mid], a[high] = a[high], a[mid]
            high -= 1

# Example usage
a = [2, 0, 1, 2, 1, 0, 0, 2]
sort(a)
print(a)  # Output: [0, 0, 0, 1, 1, 2, 2, 2]
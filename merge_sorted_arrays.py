def merge(arr1, arr2):
    m, n = len(arr1), len(arr2)

    i, j = m - 1, 0

    # Step 1: Swap if needed
    while i >= 0 and j < n:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1

    # Step 2: Sort both arrays
    arr1.sort()
    arr2.sort()


# Example
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

merge(arr1, arr2)

print("arr1 =", arr1)
print("arr2 =", arr2)
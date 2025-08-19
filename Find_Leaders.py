def find_leaders(arr):
    n = len(arr)
    leaders = []

    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range (n-2, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]


    leaders.reverse()
    return leaders  

arr = [16, 17, 4, 3, 5, 2]
print("leaders:", find_leaders(arr))      
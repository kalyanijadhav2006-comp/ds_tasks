def zero_sum_subarrays(arr):
    result = []              # to store (start, end) pairs
    prefix_sum = 0
    seen = {0: [-1]}         # sum → list of indices

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # if we saw this sum before, then subarray between old+1 and i is zero
        if prefix_sum in seen:
            for start in seen[prefix_sum]:
                result.append((start + 1, i))
            seen[prefix_sum].append(i)
        else:
            seen[prefix_sum] = [i]

    return result


# Example
arr = [1, 2, -3, 3, -1, 2]
print(zero_sum_subarrays(arr))
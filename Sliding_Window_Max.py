from collections import deque

class Solution:
    def maxSlidingWindow(self, arr, k):
        n = len(arr)
        dq = deque() 
        result = []

        for i in range(n):
            
            if dq and dq[0] <= i - k:
                dq.popleft()

            
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()

            dq.append(i)

            
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result



arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
sol = Solution()
print(sol.maxSlidingWindow(arr, k))
class Solution:
    @staticmethod
    def subarraySum(arr, target):
        """
        Given an array arr[] containing only non-negative integers,
        your task is to find a continuous subarray (a contiguous sequence of elements) 
        whose sum equals a specified value target. You need to return the 1-based indices
        of the leftmost and rightmost elements of this subarray. You need to find the first
        subarray whose sum is equal to the target.
        Note: If no such array is possible then, return [-1].
        Input: arr[] = [1, 2, 3, 7, 5], target = 12
        Output: [2, 4]
        Explanation: The sum of elements from 2nd to 4th position is 12.
        """
        i = 0
        j = i + 1
        while i < len(arr) and j < len(arr):
            if arr[i] < arr[j]:
                result = arr[i] + arr[j]
                if result == target:
                    return [i, j]
                else:
                    result = 0
                    j += 1 
                    i += 1 
                    result = arr[i]+arr[j]
                    if result == target:
                        return [i, j]
                j += 1 
                i += 1 
            if i == (len(arr)-1):
                return [-1]
    @staticmethod
    def subarraySum_ia(arr, target):
        """
        Finds the first continuous subarray whose sum equals the target 
        using the O(N) Sliding Window technique.
        Returns the 1-based indices [start, end] or [-1].
        """
        # Pointers for the start and end of the current window
        start = 0
        current_sum = 0
        n = len(arr)

        # 'end' pointer iterates through the array, expanding the window
        for end in range(n):
            # 1. Expand the window: Add the new element to the current sum
            current_sum += arr[end]

            # 2. Shrink the window: If the sum exceeds the target, slide the 
            #    start pointer forward until the sum is manageable again.
            #    This loop condition (current_sum > target) is key for non-negative numbers.
            while current_sum > target and start <= end:
                current_sum -= arr[start]
                start += 1  # Shrink the window from the left

            # 3. Check for the Target Match
            if current_sum == target:
                # The subarray is found! Return the 1-based indices.
                # Start index is (start + 1) and End index is (end + 1).
                return [start + 1, end + 1]

        # If the loop finishes without finding a match
        return [-1]

ob = Solution.subarraySum([1, 2, 3, 7, 5], 12)
print(ob)
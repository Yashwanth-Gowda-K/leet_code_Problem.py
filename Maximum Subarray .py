"""Description:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""


"""Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

def maxSubArray(nums):
    current_sum = max_sum = nums[0]  # Initialize current_sum to the first element of nums

    for num in nums[1:]:
        current_sum = max(num , current_sum + num)
        max_sum = max(max_sum, current_sum) # Update max_sum if current_sum is greater

    return max_sum  # Return the maximum sum found


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))  # Output: 6
# The function maxSubArray takes an array of integers as input and returns the maximum sum of a contiguous subarray.    

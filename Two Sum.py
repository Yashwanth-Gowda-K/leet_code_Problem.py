"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order."""


      # Soultion
"""The problem is simple. You're given a list of integers and a target value. 
You need to return the indices of two numbers that add up to the target.
There's always exactly one solution and you can't use the same number twice."""


""" if thr input list is [2,7,11,15] and the target is 9,
the output should be [0,1] because nums[0] + nums[1] = 2 + 7 = 9."""


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Dictionary to store the indices of the numbers seen

        # Looping through list with index and value
        for i , num in enumerate(nums):
            complement = target - num # Calculate the number needed to reach the target

            #We will check if that number has been seee
            if complement in seen:
                  return [seen[complement], i] # Return both indices if it found 
            
            seen[num] = i # othwise, store the current number and its index

            return [] # If no solution is found, return an empty list (though the problem guarantees one solution)
      

""" Time Complexity: O(n) - We go through the list once.
Space Complexity: O(n) - We store the indices in a dictionary.""" 


""" Time Complexity: O(n)
We iterate over the list only once, and each lookup/insertion in the hash map (dict) is O(1) on average.

So if n is the number of elements in nums, the whole algorithm runs in linear time.

🧠 Space Complexity: O(n)
We're using extra space for the seen dictionary.

In the worst case (where no two numbers add up to the target until the end), the dictionary stores all n numbers,
 making the space complexity O(n)."""
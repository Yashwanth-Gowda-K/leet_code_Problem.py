from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # Convert each list to a set to remove duplicates
        set1, set2, set3 = set(nums1), set(nums2), set(nums3)
        
        # Dictionary to count occurrences across sets
        count = {}
        
        # Count numbers in set1
        for num in set1:
            count[num] = count.get(num, 0) + 1
        
        # Count numbers in set2
        for num in set2:
            count[num] = count.get(num, 0) + 1
        
        # Count numbers in set3
        for num in set3:
            count[num] = count.get(num, 0) + 1
        
        # Return numbers appearing in 2 or more sets
        return [num for num, freq in count.items() if freq >= 2]

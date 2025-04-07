class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets to remove duplicates and allow fast intersection
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the intersection of the two sets
        result = set1 & set2  # or: set1.intersection(set2)
        
        # Return the result as a list
        return list(result)

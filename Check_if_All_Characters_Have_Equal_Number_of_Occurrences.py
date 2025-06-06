from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        # Get the first frequency to compare others against
        first_count = next(iter(freq.values()))
        
        # Check if all counts match the first one
        return all(count == first_count for count in freq.values())

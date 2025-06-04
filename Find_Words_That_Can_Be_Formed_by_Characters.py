from collections import Counter

class Solution:
    def countCharacters(self, words, chars):
        # Count how many of each letter we have
        chars_count = Counter(chars)
        total = 0
        
        for word in words:
            # Count letters needed for this word
            word_count = Counter(word)
            
            # Check if we have enough of each letter
            valid = True
            for char in word_count:
                if word_count[char] > chars_count[char]:
                    valid = False
                    break
            
            if valid:
                total += len(word)
        
        return total

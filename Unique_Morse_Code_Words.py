class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]        

        unique_morse = set()  # Stores unique Morse codes

        for word in words:
            morse_word = []  # Stores Morse code for current word
            for char in word:
                # Convert char to Morse code using ASCII math:
                # 'a' → 97, so ord(char) - ord('a') gives index (e.g., 'g' → 103 - 97 = 6)
                morse_word.append(morse_codes[ord(char) - ord('a')])
            
            # Join Morse letters into a single string and add to set
            unique_morse.add(''.join(morse_word))
        
        # Number of unique Morse codes
        return len(unique_morse)

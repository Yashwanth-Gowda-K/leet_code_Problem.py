"Here's the problem: You're given a string that only contains the characters (), {}, and []."
"You need to return True if the brackets are all matched properly and closed in the correct order."
" Otherwise, return False."

"""Input: "()[]{}" → Output: True  
Input: "(]"     → Output: False  
Input: "([)]"   → Output: False  
Input: "{[]}"   → Output: True
"""
""" Input: "{[()]}"
Step 1: Push '{'     → stack: ['{']
Step 2: Push '['     → stack: ['{', '[']
Step 3: Push '('     → stack: ['{', '[', '(']
Step 4: Found ')'    → Pop '(', match → ✅
Step 5: Found ']'    → Pop '[', match → ✅
Step 6: Found '}'    → Pop '{', match → ✅
Final stack: [] → return True
"""


def isValid(s: str) -> bool:
    stack = [] #To store the opening brackets
    mapping = {")": "(", "}": "{", "]": "["} # mapping closing brackets to their corresponding opening brackets
    #loop through each character in the string
    for char in s: # The time
        if char in mapping: #if the character is a closing bracket
            #pop the top most element from the stack if it exists, otherwise assign a dummy value '#'
            top_element = stack.pop() if stack else '#'
            #check if the top of the stack matches the current closing bracket
            if mapping[char] != top_element:
                return False #Not a match
        else:
            #if is's a opening bracket, push it onto the stack
            stack.append(char)
    #if the stack is empty, all brackets were matched properly and closed in the correct order
    return not stack 


""" Time & Space Complexity
"Time Complexity is O(n) — we loop through the string once.
Space Complexity is O(n) — in the worst case, the stack holds all opening brackets."

"""


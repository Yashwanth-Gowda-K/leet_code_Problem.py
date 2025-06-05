from collections import defaultdict

def uniqueOccurrences(arr: list[int]) -> bool:
    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1
    
    # Check if all frequencies are unique
    return len(freq.values()) == len(set(freq.values()))

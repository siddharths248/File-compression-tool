from collections import defaultdict

def bwtDecode(bwtInput: str, ogIdx: int) -> str:
    length = len(bwtInput)
    
    sorted_bwt = sorted(bwtInput)
    
    rank = defaultdict(int)
    last_column = list(bwtInput)
    first_occurrence = {}  # Tracks first occurrence of each character in sorted_bwt
    
    for i, char in enumerate(sorted_bwt):
        if char not in first_occurrence:
            first_occurrence[char] = i
    
    next_row = [0] * length
    count = defaultdict(int)
    for i in range(length):
        char = last_column[i]
        next_row[i] = first_occurrence[char] + count[char]
        count[char] += 1
    
    # Step 4: Reconstruct the original string (in reverse)
    result = []
    current_row = ogIdx
    for _ in range(length):
        result.append(last_column[current_row])
        current_row = next_row[current_row]
    
    # Remove the end marker and reverse
    decoded = ''.join(reversed(result)).rstrip('\0')
    return decoded
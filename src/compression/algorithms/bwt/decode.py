from collections import defaultdict

def bwtDecode(bwtInput: bytes, ogIdx: int, endMarker: int = 0) -> bytes:

    if not bwtInput:
        return b''
    
    if endMarker not in bwtInput:
        raise ValueError("End marker not found in BWT bytes")
    if not (0<=ogIdx< len(bwtInput)):
        raise ValueError("original index out of bounds for BWT decode")
    
    length = len(bwtInput)
    
    sorted_bwt = sorted(bwtInput)
    
    rank = defaultdict(int)
    # last_column = list(bwtInput)
    first_occurrence = {}  # Tracks first occurrence of each character in sorted_bwt
    
    for i, char in enumerate(sorted_bwt):
        if char not in first_occurrence:
            first_occurrence[char] = i
    
    next_row = [0] * length
    count = defaultdict(int)
    for i in range(length):
        char = bwtInput[i]
        next_row[i] = first_occurrence[char] + count[char]
        count[char] += 1
    
    # Step 4: Reconstruct the original string (in reverse)
    result = bytearray()
    current_row = ogIdx
    for _ in range(length):
        result.append(bwtInput[current_row])
        current_row = next_row[current_row]
    
    # Remove the end marker and reverse
    decodedBytes = bytes(reversed(result))

    if decodedBytes and decodedBytes[-1]==endMarker:
        return decodedBytes[:-1]
    
    return decodedBytes
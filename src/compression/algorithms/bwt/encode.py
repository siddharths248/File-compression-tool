
def pick_end_marker(s, pref=('$', '\0', chr(1), chr(2))):
    for marker in pref:
        if marker not in s:
            return marker
    raise ValueError("No suitable end marker found in input.")



def bwtEncode(data : bytes, endMarker: int=0):

    if not (0 <= endMarker <= 255):
        raise ValueError("End marker must be a single byte value (0-255).")
    if endMarker in data:

        for candidate in range(256):
            if candidate not in data:
                endMarker = candidate
                break
        else:
            raise ValueError("No suitable end marker found in input data.") 

    data += bytes([endMarker])
    n = len(data)
    
    table = [data[i:] + data[:i] for i in range(n)]
    tableSorted = sorted(table)
    lastColumn = bytes(row[-1] for row in tableSorted)
    ogIdx = tableSorted.index(data)

    return lastColumn, ogIdx, endMarker

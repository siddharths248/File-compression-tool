
def pick_end_marker(s, pref=('$', '\0', chr(1), chr(2))):
    for marker in pref:
        if marker not in s:
            return marker
    raise ValueError("No suitable end marker found in input.")



def bwtEncode(s : str, endMarker: str=None):

    if not isinstance(s,str):
        raise TypeError("Input must be a string")
    if endMarker is None:
        endMarker = pick_end_marker(s)
    if endMarker in s:
        raise ValueError(f"End marker '{endMarker}' found in input")

    s += endMarker

    if not s:
        return "",0
    
    table = [s[i:] + s[:i] for i in range(len(s))]
    tableSorted = sorted(table)
    lastColumn = [row[-1] for row in tableSorted]
    ogIdx = tableSorted.index(s)

    return (''.join(lastColumn),ogIdx, endMarker)


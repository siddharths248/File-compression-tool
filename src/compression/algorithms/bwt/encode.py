
def bwtEncode(s : str):

    s = s + '\0'
    table = [s[i:] + s[:i] for i in range(len(s))]
    tableSorted = sorted(table)
    lastColumn = [row[-1] for row in tableSorted]
    ogIdx = tableSorted.index(s)

    return (''.join(lastColumn),ogIdx)



def mtfEncode(s):

    symbols = list(dict.fromkeys(s))
    table = symbols.copy()
    result = []

    for char in s:
        idx = table.index(char)
        result.append(idx)

        table.pop(idx)
        table.insert(0,char)

    return (result, symbols)


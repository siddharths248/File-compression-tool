
def mtfEncode(s):

    if not isinstance(s,str):
        raise TypeError("Input must be a string")
    
    if not s:
        return ([],[])


    symbols = list(dict.fromkeys(s))
    table = symbols.copy()
    result = []

    for char in s:
        
        if char not in table:
            raise ValueError(f"Symbol '{char}' not found in symbol table")

        idx = table.index(s)
        result.append(idx)

        table.pop(idx)
        table.insert(0,char)
    
    return (result,symbols)

    



def mtfEncode(data : bytes):

    if not isinstance(data, (bytes, bytearray())):
        raise TypeError("Input must be bytes or bytearray")
    
    if not data:
        return ([],[])


    symbols = list(dict.fromkeys(data))
    table = symbols.copy()
    result = []

    for byte in data:
        
        if byte not in table:
            raise ValueError(f"Symbol '{byte}' not found in symbol table")

        idx = table.index(byte)
        result.append(idx)

        table.pop(idx)
        table.insert(0,byte)
    
    return (result,symbols)

    


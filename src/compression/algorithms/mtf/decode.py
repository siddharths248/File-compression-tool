
def mtfDecode(indices, symbolTable):

    if not symbolTable or not indices:
        return ""
    

    table = list(symbolTable)
    output = []

    for idx in indices:
        
        if not isinstance(idx,int):
            raise TypeError(f"Index '{idx}' is not an integer")
        if idx<0 or idx>=len(table):
            raise ValueError(f"Index '{idx}' out of bounds")
        char = table[idx]
        output.append(char)

        table.pop(idx)
        table.insert(0,char)

    return ''.join(output)
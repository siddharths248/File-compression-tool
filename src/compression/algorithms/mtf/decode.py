
def mtfDecode(indices, symbolTable):

    table = list(symbolTable)
    output = []

    for idx in indices:
        char = table[idx]
        output.append(char)

        table.pop(idx)
        table.insert(0,char)

    return ''.join(output)
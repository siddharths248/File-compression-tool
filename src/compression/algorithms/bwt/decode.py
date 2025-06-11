
def bwtDecode(bwtInput, ogIndex):

    length = len(bwtInput)
    table = ['']*length

    for itr in range(length):
        table = sorted([bwtInput[i] + table[i]] for i in range(length))
    s = table[ogIndex]
    return (s.rstrip('\0'))
from .tree import HuffmanNode
from bitarray import bitarray

class HuffmanDecoder:


    def __init__(self, treeRoot=None, codesList=None):
        self.treeRoot = treeRoot
        self.codesList = codesList
    
    def setTreeRoot(self, treeRoot):
        self.treeRoot = treeRoot
    
    def setCodesList(self, codesList):
        self.codesList = codesList


    def decode(self,encodedData: bytes, bit_length: int) -> bytes:

        if self.treeRoot is None:
            if encodedData == b"":
                return b""
            raise ValueError("Huffman tree must be set before decoding")
        bits = bitarray()
        bits.frombytes(encodedData)
        bits = bits[:bit_length]
        bitStr = bits.to01
        

        decodedChars = []

        node = self.treeRoot

        if node.isLeaf():
            return bytes([node.char]*len(bitStr))
        for bit in bitStr:
            if bit=='0':
                node = node.left
            elif bit=='1':
                node = node.right
            else:
                raise ValueError(f"Invalid bit in encoded data: '{bit}'")
            
            if node.isLeaf():
                decodedChars.append(node.char)
                node = self.treeRoot
        return bytes(decodedChars)
    
    
    def decodeWithCodesList(self, encodedData: bytes, bit_length: int) -> bytes:

        #decodes encoded data using codesList
        if (self.codesList is None):
            raise ValueError("CodesList must be set before decoding")

        
        code = ''
        code_to_byte = {v : k for (k,v) in self.codesList.items()}

        bits = bitarray()
        bits.frombytes(encodedData)
        bits = bits[:bit_length]

        decodedChars = bitarray.decode(bits, self.codesList)

        return bytes(decodedChars)
    

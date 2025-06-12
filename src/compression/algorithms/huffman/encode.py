from .tree import buildHuffmanTree, generateCodes
from bitarray import bitarray

class HuffmanEncoder:

    def __init__(self):
        self.frequency_table = None
        self.treeRoot = None
        self.codesList = None

    def buildFrequencyTable(self, data: bytes) -> dict:
        freq = {}
        for byte in data:
            freq[byte] = freq.get(byte,0) + 1
        self.frequency_table = freq
        return freq
    
    def encoderSetup(self, data: bytes):
        #build freq table, construct tree and codesList
        self.buildFrequencyTable(data)
        self.treeRoot = buildHuffmanTree(self.frequency_table)
        self.codesList = generateCodes(self.treeRoot)
    
    def encode(self, data: bytes) -> tuple[bytes,int]:
        #encodes input data
        if (self.codesList is None):
            self.encoderSetup(data)
        encodedString = ''.join(self.codesList[byte] for byte in data)
        bits = bitarray(encodedString)
        return bits.tobytes(),len(bits)
        return bitarray(encodedString).tobytes()
    
    def getCodesList(self) -> dict:
        return self.codesList
    
    def getTreeRoot(self):
        return self.treeRoot

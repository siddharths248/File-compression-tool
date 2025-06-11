from .tree import buildHuffmanTree, generateCodes
from bitarray import bitarray

class HuffmanEncoder:

    def __init__(self):
        self.frequency_table = None
        self.treeRoot = None
        self.codesList = None

    def buildFrequencyTable(self, data: str) -> dict:
        freq = {}
        for char in data:
            freq[char] = freq.get(char,0) + 1
        self.frequency_table = freq
        return freq
    
    def encoderSetup(self, data: str):
        #build freq table, construct tree and codesList
        self.buildFrequencyTable(data)
        self.treeRoot = buildHuffmanTree(self.frequency_table)
        self.codesList = generateCodes(self.treeRoot)
    
    def encode(self, data: str) -> bytes:
        #encodes input data
        if (self.codesList is None):
            self.encoderSetup(data)
        encodedString = ''.join(self.codesList[char] for char in data)
        return bitarray(encodedString).tobytes()
    
    def getCodesList(self) -> dict:
        return self.codesList
    
    def getTreeRoot(self):
        return self.treeRoot

from .tree import HuffmanNode

class HuffmanDecoder:


    def __init__(self, treeRoot=None, codesList=None):
        self.treeRoot = treeRoot
        self.codesList = codesList
    
    def setTreeRoot(self, treeRoot):
        self.treeRoot = treeRoot
    
    def setCodesList(self, codesList):
        self.codesList = codesList


    def decode(self,encodedData):

        #decodes encoded string using huffman tree
        if (self.treeRoot is None):
            raise ValueError("Huffman tree must be set before decoding")

        decodedChars = []

        node = self.treeRoot
        for bit in encodedData:
            if bit=='0':
                node = node.left
            else:
                node = node.right
            
            if node.isLeaf():
                decodedChars.append(node.char)
                node = self.treeRoot
        return ''.join(decodedChars)
    
    
    def decodeWithCodesList(self, encodedData):

        #decodes encoded data using codesList
        if (self.codesList is None):
            raise ValueError("CodesList must be set before decoding")

        decodedChars = []
        code = ''
        code_to_char = {v : k for (k,v) in self.codesList.items()}

        for bit in encodedData:
            code += bit
            if (code in code_to_char):
                decodedChars.append(code_to_char[code])
                code = ''
        
        return ''.join(decodedChars)
    

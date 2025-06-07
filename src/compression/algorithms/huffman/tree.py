import heapq

class HuffmanNode:

    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        pass

    def __lt__(self,other):
        return (self.freq < other.freq)

    def isLeaf(self):
        return (self.left is None) and (self.right is None)
    

def buildHuffmanTree(frequency_table):

    #builds huffman tree from frequency table
    heap = [HuffmanNode(freq,char) for (char,freq) in frequency_table.items()]
    heapq.heapify(heap)

    while (len(heap)>1):
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        mergedNode = HuffmanNode(left.freq+right.freq, left = left, right=right)
        heapq.heappush(heap,mergedNode)
    
    if heap:
        return heap[0]
    else:
        return None


def generateCodes(node, prefix='', codesList = None):

    #generates huffman codes for each character from tree root
    if (codesList is None):
        codesList = {}

    if (node is not None):
        if (node.char is not None):
            codesList[node.char] = prefix
        else:
            generateCodes(node.left, prefix+'0', codesList)
            generateCodes(node.right, prefix+'1', codesList)
    return codesList
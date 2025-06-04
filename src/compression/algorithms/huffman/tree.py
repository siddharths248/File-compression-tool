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
    
    
    
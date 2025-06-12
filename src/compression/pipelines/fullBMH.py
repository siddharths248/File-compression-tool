from compression.algorithms.bwt.encode import bwtEncode
from compression.algorithms.bwt.decode import bwtDecode
from compression.algorithms.mtf.encode import mtfEncode
from compression.algorithms.mtf.decode import mtfDecode
from compression.algorithms.huffman.encode import HuffmanEncoder
from compression.algorithms.huffman.decode import HuffmanDecoder


class BWTMTFHuffmanPipeline:

    def __init__(self):
        self.metadata = {}
    

    def compress(self, chunk: bytes) -> bytes:

        bwtBytes, self.metadata["bwtIndex"], self.metadata["endMarker"] = bwtEncode(chunk)

        mtfIndices, self.metadata["symbolTable"] = mtfEncode(bwtBytes)

        encoder = HuffmanEncoder()

        encodedBytes, self.metadata["bitLength"] = encoder(mtfIndices)

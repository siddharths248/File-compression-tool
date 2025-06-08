import unittest
from compression.algorithms.huffman.encode import HuffmanEncoder
from compression.algorithms.huffman.decode import HuffmanDecoder
from compression.algorithms.huffman.tree import buildHuffmanTree, generateCodes

class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.sample_text = "abracadabra"
        self.encoder = HuffmanEncoder()
        self.encoded = self.encoder.encode(self.sample_text)
        self.codesList = self.encoder.getCodesList()
        self.treeRoot = self.encoder.getTreeRoot()
        self.decoder = HuffmanDecoder(treeRoot=self.treeRoot, codesList=self.codesList)

    def test_frequency_table(self):
        freq_table = self.encoder.buildFrequencyTable(self.sample_text)
        self.assertIsInstance(freq_table, dict)
        self.assertEqual(freq_table['a'], 5)
        self.assertEqual(freq_table['b'], 2)
        self.assertEqual(freq_table['r'], 2)
        self.assertEqual(freq_table['c'], 1)
        self.assertEqual(freq_table['d'], 1)

    def test_encoding_and_decoding_with_tree(self):
        decoded = self.decoder.decode(self.encoded)
        self.assertEqual(decoded, self.sample_text)

    def test_encoding_and_decoding_with_codesList(self):
        decoded = self.decoder.decodeWithCodesList(self.encoded)
        self.assertEqual(decoded, self.sample_text)

    def test_codesList_is_prefix_free(self):
        codes = list(self.codesList.values())
        for i, code1 in enumerate(codes):
            for j, code2 in enumerate(codes):
                if i != j:
                    self.assertFalse(code1.startswith(code2))

    def test_empty_string(self):
        empty_encoder = HuffmanEncoder()
        encoded = empty_encoder.encode("")
        self.assertEqual(encoded, "")
        empty_decoder = HuffmanDecoder(treeRoot=empty_encoder.getTreeRoot(), codesList=empty_encoder.getCodesList())
        decoded = empty_decoder.decode(encoded)
        self.assertEqual(decoded, "")

    def test_invalid_bit_in_encoded_data(self):
        invalid_encoded = "02a1"
        with self.assertRaises(ValueError):
            self.decoder.decode(invalid_encoded)

    def test_single_character(self):
        encoder = HuffmanEncoder()
        encoded = encoder.encode("aaaaa")
        decoder = HuffmanDecoder(
            treeRoot=encoder.getTreeRoot(),
            codesList=encoder.getCodesList()
        )
        decoded = decoder.decode(encoded)
        self.assertEqual(decoded, "aaaaa")

if __name__ == '__main__':
    unittest.main()

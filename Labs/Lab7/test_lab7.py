import lab7 
import unittest

class TestCases(unittest.TestCase):

    def assert_tuple_equal(self, expected, actual):
        self.assertEqual(type(expected), type(actual))
        self.assertEqual(len(expected), len(actual))
        if len(actual):
            self.assertEqual(expected[0], actual[0])  # check they have the same string
            self.assertEqual(expected, actual)

    def test_lagrassian_cipher_complex(self):
        k = 5
        f_out = lab7.lagrassian_cipher(("Jamil", "is", "cool"), k)
        self.assert_tuple_equal(f_out,('O\\hdq', 'dn', '^jjq') )
        f_out_x2 = lab7.lagrassian_cipher(('O\\hdq', 'dn', '^jjq'), k)
        self.assert_tuple_equal(f_out_x2,("Jamil", "is", "cool") )
        self.assertEqual(lab7.lagrassian_cipher(f_out, k), f_out_x2)


    def test_lagrassian_cipher_simple_char_public(self):
        f_out = lab7.lagrassian_cipher(("a",), 1)
        self.assert_tuple_equal(f_out,('`',) )

        f_out_b = lab7.lagrassian_cipher(("b",), 1)
        self.assert_tuple_equal(f_out_b,('c',) )


    def test_lagrassian_cipher_simple_word_public(self):
        f_out = lab7.lagrassian_cipher(("abc",), 1)
        self.assert_tuple_equal(f_out,('`cb',))


    def test_lagrassian_cipher_multiple_words(self):
        f_out = lab7.lagrassian_cipher(("hey", "there", "chat"), 13)
        self.assert_tuple_equal(f_out,('uXl', '\x81uX\x7fX', 'VuT\x81'))
        f_outx2 = lab7.lagrassian_cipher(f_out, 25)
        self.assert_tuple_equal(f_outx2, ('\\q\x85', 'h\\qfq', 'o\\mh'))
        F_outDecode = lab7.lagrassian_cipher(f_outx2, 25)

        self.assert_tuple_equal(F_outDecode,('uXl', '\x81uX\x7fX', 'VuT\x81') )
        F_outDecodex2 = lab7.lagrassian_cipher(F_outDecode, 13)
        self.assert_tuple_equal(F_outDecodex2, ("hey", "there", "chat") )

    def test_lagrassian_cipher_simple_char_hidden(self):
        f_out_c = lab7.lagrassian_cipher(("c",), 1)
        self.assert_tuple_equal(f_out_c,('b',) )

    def test_lagrassian_cipher_simple_word_hidden(self):
        f_out3 = lab7.lagrassian_cipher(("abc",), 3)
        self.assert_tuple_equal(f_out3,('^e`',))

if __name__ == "__main__":
    unittest.main()

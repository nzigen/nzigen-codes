import unittest

from nzigen_low_level.base.padding import unpad, pad


class TestPadding(unittest.TestCase):

    def setUp(self):
        pass

    def test_unpad(self):
        self.assertEqual(b'1234', unpad('1234\x04\x04\x04\x04'))
        self.assertEqual(b'abcd', unpad(b'abcd\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'))
        self.assertEqual(b'111111', unpad('111111\06\06\06\06\06\06'))

    def test_pad(self):
        self.assertEqual(b'1234\x04\x04\x04\x04', pad('1234', 8))
        self.assertEqual(b'abcd\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c', pad(b'abcd', 16))
        self.assertEqual(b'111111\06\06\06\06\06\06', pad('111111', 6))

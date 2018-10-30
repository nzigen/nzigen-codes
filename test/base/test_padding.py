import unittest

from base.padding import pad, unpad


class TestPadding(unittest.TestCase):

    def setUp(self):
        pass

    def test_unpad(self):
        self.assertEqual('1234', unpad('1234\x04\x04\x04\x04'))
        self.assertEqual('abcd', unpad('abcd\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'))
        self.assertEqual('111111', unpad('111111\06\06\06\06\06\06'))

    def test_pad(self):
        self.assertEqual('1234\x04\x04\x04\x04', pad('1234', 8))
        self.assertEqual('abcd\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c', pad('abcd', 16))
        self.assertEqual('111111\06\06\06\06\06\06', pad('111111', 6))

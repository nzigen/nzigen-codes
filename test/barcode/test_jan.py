import unittest

from barcode.jan import modulus_10_weight_3


class TestJan(unittest.TestCase):

    def setUp(self):
        pass

    def test_modulus_10_weight_3(self):
        self.assertEqual(4, modulus_10_weight_3('491234567890'))
        self.assertEqual(2, modulus_10_weight_3('351386327796'))

import unittest

from nzigen_codes.encryption.aes import encrypt_text, decrypt_text


class TestAes(unittest.TestCase):

    def setUp(self):
        pass

    def test_encryption_of_text(self):
        key0 = 'Sooph%e0otaGh|ah'
        self.assertEqual('1234', decrypt_text(key0, encrypt_text(key0, '1234')).decode("utf-8"))

        key1 = 'Ohh/ah7eNee9thoh'
        self.assertEqual('Hello, world!', decrypt_text(key1, encrypt_text(key1, 'Hello, world!')).decode("utf-8"))
        self.assertEqual('こんにちは、世界。', decrypt_text(key1, encrypt_text(key1, 'こんにちは、世界。')).decode("utf-8"))

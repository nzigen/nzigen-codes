import unittest


class TestIsbn(unittest.TestCase):

    def setUp(self):
        pass

    def test_convert_isbn_10_to_isbn_13(self):
        from nzigen_low_level.barcode.isbn import convert_isbn_10_to_isbn_13
        self.assertEqual('', convert_isbn_10_to_isbn_13('48855209'))
        self.assertEqual('9784885520907', convert_isbn_10_to_isbn_13('488552090'))
        self.assertEqual('9784885520907', convert_isbn_10_to_isbn_13('4885520908'))
        self.assertEqual('9784061529243', convert_isbn_10_to_isbn_13('4061529242'))


    def test_convert_isbn_to_asin(self):
        pass
        # from nzigen_low_level.barcode.isbn import convert_isbn_to_asin
        # self.assertEqual(4, convert_isbn_to_asin('491234567890'))
        # self.assertEqual(2, convert_isbn_to_asin('351386327796'))

    def test_generate_isbn_10_check_digit(self):
        from nzigen_low_level.barcode.isbn import generate_isbn_10_check_digit
        self.assertEqual('', generate_isbn_10_check_digit('40628203'))
        self.assertEqual('2', generate_isbn_10_check_digit('406282038'))
        self.assertEqual('8', generate_isbn_10_check_digit('488552090'))
        self.assertEqual('X', generate_isbn_10_check_digit('462781741'))


    def test_generate_isbn_13_check_digit(self):
        from nzigen_low_level.barcode.isbn import generate_isbn_13_check_digit
        self.assertEqual('', generate_isbn_13_check_digit('97848855209'))
        self.assertEqual('7', generate_isbn_13_check_digit('978488552090'))
        self.assertEqual('8', generate_isbn_13_check_digit('978-462781741'))

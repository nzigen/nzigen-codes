# -*- coding: utf-8 -*-
import re


def convert_isbn_to_asin(code):
    """
    TODO
    :rtype: str
    """
    return code


def convert_isbn_10_to_isbn_13(code):
    numeric = re.sub(r'\D', r'', str(code))
    if len(numeric) < 9:
        return ''
    numeric = '978' + numeric[0:9]
    digit = generate_isbn_13_check_digit(numeric)
    if len(digit) == 0:
        return ''
    return numeric + digit


def generate_isbn_10_check_digit(code):
    """
    isbn10 のチェックディジットを返す。
    c9 = 11 - (c0x10 + c1x9 + c2x8 + c3x7 + c4x6 + c5x5 + c6x4 + c7x3 + c8x2) % 11
    ただし c9=10 のときは 'X' を返す。
    :rtype: str
    """
    numeric = re.sub(r'\D', r'', str(code))
    if len(numeric) < 9:
        return ''
    digit = 0
    for index, number in enumerate(numeric[0:9]):
        digit += int(number) * (10 - index)
    digit = 11 - (digit % 11)
    if digit == 10:
        return 'X'

    return str(digit)


def generate_isbn_13_check_digit(code):
    """
    isbn10 のチェックディジットを返す。
    c12 = 10 - (c0x1 + c1x3 + c2x1 + c3x3 + ...) % 10
    :rtype: str
    """
    numeric = re.sub(r'\D', r'', str(code))
    if len(numeric) < 12:
        return ''
    digit = 0
    for index, number in enumerate(numeric[0:12]):
        digit += int(number) * ((index % 2) * 2 + 1)
    digit = 10 - (digit % 10)

    return str(digit)

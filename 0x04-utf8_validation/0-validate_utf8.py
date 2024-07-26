#!/usr/bin/python3
"""
Module to determine if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if the given list of integers represents a valid UTF-8 encoding.

    Each integer in the list represents a byte (0 to 255).
    The function verifies
    if these bytes form a valid UTF-8 encoded sequence, where UTF-8 characters
    can be 1 to 4 bytes long.

    Args:
        data (list): A list of integers, where each integer represents a byte.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    bytes_needed = 0

    for byte in data:
        current_byte = byte & 0xFF

        if bytes_needed == 0:
            if current_byte < 0x80:
                bytes_needed = 1
            elif current_byte & 0b11100000 == 0b11000000:
                bytes_needed = 2
            elif current_byte & 0b11110000 == 0b11100000:
                bytes_needed = 3
            elif current_byte & 0b11111000 == 0b11110000:
                bytes_needed = 4
            else:
                return False
        else:
            if current_byte & 0b11000000 != 0b10000000:
                return False

        bytes_needed -= 1

    return bytes_needed == 0

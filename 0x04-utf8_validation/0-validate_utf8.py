#!/usr/bin/python3
"""UTF-8 encoding"""


def validUTF8(data):
    """
    Method to determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    for num in data:
        # Mask to get only the last 8 bits (1 byte)
        byte = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1's
            if (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check if the byte starts with '10'
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0

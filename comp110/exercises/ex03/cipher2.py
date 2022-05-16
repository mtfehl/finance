"""EX03: If and While statements."""
__author__ = "730321206"

ASCII_INT_LOWER: int = 97
REMAINDER: int = 26
ASCII_INT_UPPER: int = 65
letters: str = "abcdefghijklmnopqrstuvwxyz"


def encode_char(x: str) -> str:
    """Returns the following sequential letter."""
    ascii_code: int = ord(x)
    if ascii_code >= 97:
        normal_code: int = ascii_code - ASCII_INT_LOWER
        encoded_code: int = (normal_code + 1) % REMAINDER + ASCII_INT_LOWER
        encoded_character: str = (chr(encoded_code)).lower()
        return encoded_character
    else:
        upper_code: int = ascii_code - ASCII_INT_UPPER
        encoded_ucode: int = (upper_code + 1) % REMAINDER + ASCII_INT_UPPER
        encoded_ucharacter: str = (chr(encoded_ucode)).upper()
        return encoded_ucharacter


def encode_str(letters: str) -> str:
    """Returns the following sequential letters encoded."""
    i: int = 0
    letter: str = ""
    while i < len(letters):
        letter: str = (letter + encode_char(letters[i]))
        i = i + 1
    return letter


def decode_char(x: str) -> str:
    """Returns the deciphered Caesar code with the previous sequential number."""
    ascii_code: int = ord(x)
    if ascii_code >= 97:
        normal_decode: int = ascii_code - ASCII_INT_LOWER
        decoded_code: int = (normal_decode - 1) % REMAINDER + ASCII_INT_LOWER
        decoded_character: str = (chr(decoded_code)).lower()
        return decoded_character
    else:
        normal_udecode: int = ascii_code - ASCII_INT_UPPER
        decoded_ucode: int = (normal_udecode - 1) % REMAINDER + ASCII_INT_UPPER
        decoded_ucharacter: str = (chr(decoded_ucode)).upper()
        return decoded_ucharacter


def decode_str(letters: str) -> str:
    """Returns the deciphered Caesar code with the previous sequential letters."""
    i: int = 0
    letter: str = ""
    while i < len(letters):
        letter: str = (letter + decode_char(letters[i]))
        i = i + 1
    return letter
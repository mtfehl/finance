"""practicing caesar ciphering ex02 (rip Caesar man)."""
__author__ = "730321206"

ASCII_INT: int = 97
REMAINDER: int = 26


def encode_char(x: str) -> str:
    """Returns the following sequential letter."""
    some_variable_name: str = x.lower()
    ascii_code: int = ord(some_variable_name)
    normal_code: int = ascii_code - ASCII_INT
    encoded_code: int = (normal_code + 1) % REMAINDER + ASCII_INT
    encoded_character: str = chr(encoded_code)
    return encoded_character


def encode_str(wxyz: str) -> str:
    """Returns the following sequential letters."""
    letter_one: str = encode_char(wxyz[0])
    letter_two: str = encode_char(wxyz[1])
    letter_three: str = encode_char(wxyz[2])
    letter_four: str = encode_char(wxyz[3])
    all_letters: str = (letter_one + letter_two + letter_three + letter_four)
    return all_letters


def decode_char(x: str) -> str:
    """Returns the deciphered Caesar code with the previous sequential number."""
    some_variable_name: str = x.lower()
    ascii_code: int = ord(some_variable_name)
    normal_code: int = ascii_code - ASCII_INT
    encoded_code: int = (normal_code - 1) % REMAINDER + ASCII_INT
    encoded_character: str = chr(encoded_code)
    return encoded_character


def decode_str(wxyz: str) -> str:
    """Returns the deciphered Caesar code with the previous sequential number."""
    letter_one: str = decode_char(wxyz[0])
    letter_two: str = decode_char(wxyz[1])
    letter_three: str = decode_char(wxyz[2])
    letter_four: str = decode_char(wxyz[3])
    all_letters: str = (letter_one + letter_two + letter_three + letter_four)
    return all_letters
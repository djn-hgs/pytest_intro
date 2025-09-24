import string

class VigenereCipher:
    def __init__(self, keyword):
        pass

    @staticmethod
    def _get_alphabetic_index(char):
        if char in string.ascii_lowercase:
            char_index = string.ascii_lowercase.index(char)

        elif char in string.ascii_uppercase:
            char_index = string.ascii_uppercase.index(char)

        else:
            raise ValueError()

        return char_index

    @staticmethod
    def _combine_character(plaintext_char, offset_char):
        pass

    def _extend_keyword(self, rqd_length):
        pass

    def encode(self, plaintext):
        pass

    @staticmethod
    def _separate_character(cipher_char, keyword_char):
        pass

    def decode(self, ciphertext):
        pass


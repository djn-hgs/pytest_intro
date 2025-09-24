import string

class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword

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

        source_index = VigenereCipher._get_alphabetic_index(plaintext_char)
        offset_index = VigenereCipher._get_alphabetic_index(offset_char)

        # This maps the cipher character forward by the offset

        target_index = (source_index + offset_index) % len(string.ascii_uppercase)

        return string.ascii_uppercase[target_index]

    def _extend_keyword(self, rqd_length):
        extended_keyword = ''

        for i in range(rqd_length):
            pos = i % len(self.keyword)
            extended_keyword += self.keyword[pos]

        return extended_keyword

    def encode(self, plaintext):
        target = ''

        extended_keyword = self._extend_keyword(len(plaintext))

        for plaintext_char, offset_char in zip(plaintext, extended_keyword):
            target += self._combine_character(plaintext_char, offset_char)

        return target

    @staticmethod
    def _separate_character(cipher_char, keyword_char):

        source_index = VigenereCipher._get_alphabetic_index(cipher_char)
        offset_index = VigenereCipher._get_alphabetic_index(keyword_char)

        # This maps the cipher character back by the offset

        target_index = (source_index - offset_index) % len(string.ascii_uppercase)

        return string.ascii_uppercase[target_index]

    def decode(self, ciphertext):
        target = ''

        extended_keyword = self._extend_keyword(len(ciphertext))

        for cipher_char, offset_char in zip(ciphertext, extended_keyword):
            target += self._separate_character(cipher_char, offset_char)

        return target


import vigenere
import pytest


class TestVigenere:

    @pytest.fixture()
    def my_cipher(self):
        return vigenere.VigenereCipher('TRAIN')

    def test_init(self, my_cipher):
        assert my_cipher.keyword == 'TRAIN'

    def test_combine_character(self, my_cipher):
        assert my_cipher._combine_character('D', 'E') == 'H'

    def test_combine_character_mod(self, my_cipher):
        assert my_cipher._combine_character('W', 'F') == 'B'

    def test_combine_lower(self, my_cipher):
        assert my_cipher._combine_character('y', 't') == 'R'

    def test_combine_non_alpha(self, my_cipher):
        with pytest.raises(ValueError):
            my_cipher._combine_character('@', 't')

    def test_simple_option(self, my_cipher):
        assert my_cipher.encode('AAAAA') == 'TRAIN'

    def test_simple_wrap(self, my_cipher):
        assert my_cipher.encode('AAAAAAA') == 'TRAINTR'

    def test_proper_no_wrap(self, my_cipher):
        assert my_cipher.encode('ENCODEINPYTHON') == 'XECWQXZNXLMYOV'

    def test__extend_keyword(self, my_cipher):
        my_cipher._extend_keyword(12)
        assert my_cipher.keyword == 'TRAINTRAINTR'

    def test__separate_character(self, my_cipher):
        assert my_cipher._separate_character('B', 'F') == 'W'


    def test_decode(self, my_cipher):
        assert my_cipher.decode('XECWQXZNXLMYOV') == 'ENCODEINPYTHON'

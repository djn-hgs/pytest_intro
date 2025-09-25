import math

import pytest

from shuffle_calc import shuffle_calc

test_data = [
    ('DEAN', math.factorial(4)),
    ('ROSALIA', math.factorial(7)/2),
    ('HERBERT', math.factorial(7)/4),
]

@pytest.mark.parametrize("name, shuffles", test_data)
def test_shuffle_calc(name, shuffles):
    assert shuffle_calc(name) == shuffles


import pytest

import grade_boundaries as gb

def test_calc_grade():
    assert gb.calc_grade(240, gb.default_boundaries) == 'A'
    assert gb.calc_grade(200, gb.default_boundaries) == 'B'

test_data = [
    (x, y)
    for x, y in gb.default_boundaries.items()
    if y is not 'Max'
]

@pytest.mark.parametrize("mark, expected", test_data)
def test_calc_grade_lots(mark, expected):
    assert gb.calc_grade(mark, gb.default_boundaries) == expected


erroneous_data = [
    -100,
    -1,
    351,
    400,
]
@pytest.mark.parametrize("mark", erroneous_data)
def test_calc_grade_erroneous(mark):
    with pytest.raises(ValueError):
        gb.calc_grade(mark, gb.default_boundaries)


def test_calc_grade_type():
    with pytest.raises(TypeError):
        gb.calc_grade('A', gb.default_boundaries)

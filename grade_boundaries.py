default_boundaries = {
350: 'Max',
298: 'A*',
239: 'A',
194: 'B',
149: 'C',
104: 'D',
60: 'E',
0: 'U'
}

def calc_grade(score: int, boundaries: dict[int, str]) -> str:

    if type(score) is not int:
        raise TypeError('score must be an integer')


    ordered_scores = sorted(boundaries.keys())

    min_score = min(ordered_scores)
    max_score = max(ordered_scores)

    if score < min_score or score > max_score:
        raise ValueError(f'score must be between {min_score} and {max_score}')

    grade = None

    for b in ordered_scores:
        if score >= b:
            if boundaries[b] != 'Max':
                grade = boundaries[b]

    return grade




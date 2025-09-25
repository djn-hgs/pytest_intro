from collections import defaultdict

import math


def shuffle_calc(to_shuffle):
    repetitions = {}


    for a in to_shuffle:
        if a in repetitions:
            repetitions[a] += 1
        else:
            repetitions[a] = 1

    denominator = math.prod(
        math.factorial(v)
        for v in repetitions.values()
    )

    return math.factorial(len(to_shuffle)) / denominator


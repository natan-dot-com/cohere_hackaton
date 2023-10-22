from typing import Tuple
import numpy as np

def discretize(range: Tuple[int, int], n_bins: int, value: float) -> int:
    assert len(range) == 2
    assert n_bins != 0

    lowerbound, upperbound = range
    factor = (upperbound - lowerbound)/n_bins

    for label, local_upperbound in enumerate(
        np.arange(lowerbound+factor, upperbound+factor, factor)
    ):
        if value <= local_upperbound:
            return label

    assert False, "unreachable"

if __name__ == "__main__":
    print(discretize((0, 1), 4, 0.95))

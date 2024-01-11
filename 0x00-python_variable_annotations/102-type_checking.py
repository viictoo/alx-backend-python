#!/usr/bin/env python3
"""This code is Validated using mypy"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """using mypy to validate

    Args:
        lst (Tuple): tuple
        factor (int, optional): integer. Defaults to 2.

    Returns:
        List: list expanded * factor
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))

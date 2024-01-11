#!/usr/bin/env python3
""" Annotating duck typing on an iterable object """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotated function with the appropriate types

    Args:
        lst (Iterable[Sequence]): itereates therefore iterable

    Returns:
        List[Tuple[Sequence, int]]: returns a list
    """
    return [(i, len(i)) for i in lst]
